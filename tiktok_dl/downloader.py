"""TikTok Video Downloader"""
import json
import os
import re
import time

import requests
import urllib3

from tiktok_dl.utils import format_utctime
from tiktok_dl.utils import match_id
from tiktok_dl.utils import search_regex
from tiktok_dl.utils import try_get
from tiktok_dl.utils import valid_url_re


class URLExistsInArchive(Exception):
    """URL Recorded in the Archive.

    Args:
        Exception (Exception): If URL is recorded in the archive.
    """

    pass


class Downloader:
    """Downloader for TikTok Videos."""

    def __init__(
        self,
        validator,
        extractor,
        logger,
        directory_prefix=None,
        dump_json=False,
        max_sleep_interval=0,
        no_check_certificate=True,
        no_overwrite=False,
        no_write_json=False,
        output_template="{Y}-{d}-{m}_{H}-{M}-{S} {id}_{user_id}",
        print_json=False,
        simulate=False,
        skip_download=False,
        sleep_interval=0.2,
        write_description=False,
        write_thumbnail=True,
    ):
        """Class for handling file downloads.

        Args:
            validator: Instance of AwemeValidator class.
            extractor: Instance of Extractor class.
            self.logger: Instance of self.logger class.
            directory_prefix (str, optional): Working directory for Downloader. Defaults to None.
            dump_json (bool, optional): Dump TikTok Video JSON and exit. Defaults to False.
            max_sleep_interval (int, optional): Maximum amount of seconds to sleep between downloads. Defaults to 0 (no sleeping).
            no_check_certificate (bool, optional): Do not validate server ssl certificates. Defaults to False.
            no_overwrite (bool, optional): Do not overwrite any file. Defaults to False.
            no_write_json (bool, optional): Do not create `.info.json` file. Defaults to False.
            output_template (str, optional): Output file template. Defaults to "{Y}-{d}-{m}_{H}-{M}-{S} {id}_{user_id}".
            print_json (bool, optional): Pretty print JSON when used with dump_json. Defaults to False.
            simulate (bool, optional): Simulate only do not write and download anything. Defaults to False.
            skip_download (bool, optional): Do not download any media. Defaults to False.
            sleep_interval (float, optional): Number of seconds to sleep between each requests. Defaults to 0.2.
            write_description (bool, optional): Create seperate .description file for description. Defaults to False.
            write_thumbnail (bool, optional): Download Video Thumbnail. Defaults to True.
        """
        self.directory_prefix = directory_prefix
        self.dump_json = dump_json
        self.max_sleep_interval = max_sleep_interval
        self.no_check_certificate = no_check_certificate
        self.no_overwrite = no_overwrite
        self.no_write_json = no_write_json
        self.output_template = output_template
        self.print_json = print_json
        self.simulate = simulate
        self.skip_download = skip_download
        self.sleep_interval = sleep_interval
        self.write_description = write_description
        self.write_thumbnail = write_thumbnail

        self.validator = validator
        self.extractor = extractor
        self.logger = logger

        self.headers = {
            "user-agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/83.0.4103.44 Safari/537.36"
            )
        }
        self.reaponse_ok = requests.codes.get("ok")

        if self.no_check_certificate:
            urllib3.disable_warnings()

    def _parse_json(self, json_string: str, video_id: str, fatal=True):
        try:
            return json.loads(json_string)
        except ValueError as ve:
            errmsg = "{}: Failed to parse JSON ".format(video_id)
            if fatal:
                raise Exception(errmsg, cause=ve)
            else:
                self.logger.error(errmsg + str(ve))

    def _download_webpage(self, url: str, video_id: str, note="Downloading webpage"):
        self.logger.debug("{} {}", note, video_id)
        r = requests.get(url, verify=self.no_check_certificate, headers=self.headers)
        return r.text

    def _fetch_data(self, url: str):
        video_id = match_id(url, valid_url_re)

        webpage = self._download_webpage(
            url, video_id, note="Downloading video webpage"
        )
        json_string = search_regex(
            r"id=\"__NEXT_DATA__\"\s+type=\"application\/json\"\s*[^>]+>\s*(?P<json_string_id>[^<]+)",
            webpage,
            "json_string",
            group="json_string_id",
        )
        json_data = self._parse_json(json_string, video_id)
        aweme_data = try_get(
            json_data, lambda x: x["props"]["pageProps"], expected_type=dict
        )

        if aweme_data.get("statusCode") != 0:
            raise FileNotFoundError("Video not available " + video_id)

        extract_version, extract_data = self.extractor.extract(json_data=aweme_data)

        return {
            "video_data": extract_data,
            "aweme_data": aweme_data,
            "tiktok-dl": extract_version,
            "timestamp": int(time.time()),
        }

    def _expand_path(self, path):
        if self.directory_prefix is None:
            return path
        return os.path.join(self.directory_prefix, path)

    def _output_format(self, json_data: dict):
        def enhance_json_data(json_data):
            data = dict(json_data)
            timestamp = data.get("create_time")
            data["Y"] = format_utctime(time=timestamp, fmt="%Y")
            data["m"] = format_utctime(time=timestamp, fmt="%m")
            data["d"] = format_utctime(time=timestamp, fmt="%d")
            data["H"] = format_utctime(time=timestamp, fmt="%H")
            data["M"] = format_utctime(time=timestamp, fmt="%M")
            data["S"] = format_utctime(time=timestamp, fmt="%S")
            return data

        enhanced = enhance_json_data(json_data)
        return self.output_template.format(**enhanced)

    def _save_json(self, data: dict, dest: str):
        if not os.path.exists(os.path.dirname(dest)):
            os.makedirs(os.path.dirname(dest))

        with open(dest, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    def _download_url(self, url: str, dest: str):
        if not os.path.exists(os.path.dirname(dest)):
            os.makedirs(os.path.dirname(dest), exist_ok=True)

        try:
            if os.path.getsize(dest) == 0:
                os.remove(dest)
        except FileNotFoundError:
            pass

        try:
            with open(dest, "xb") as handle:
                response = requests.get(url, stream=True, timeout=160)
                if response.status_code != self.reaponse_ok:
                    response.raise_for_status()

                self.logger.debug("Downloading to {}".format(dest))
                for data in response.iter_content(chunk_size=4194304):
                    handle.write(data)
                handle.close()
        except FileExistsError:
            pass
        except requests.exceptions.RequestException:
            self.logger.error("File {} not found on Server {}".format(dest, url))
            pass

        if os.path.getsize(dest) == 0:
            os.remove(dest)

    def _download_media(self, video_data: dict, filepath: str):
        video_url = video_data["play_urls"][0]
        self._download_url(video_url, self._expand_path(filepath + ".mp4"))
        cover_url = video_data["thumbnails"][0]
        self._download_url(cover_url, self._expand_path(filepath + ".jpg"))

    def download(self, url: str):
        try:
            data = self._fetch_data(url)
            self.validator.validate(data.get("video_data"))
            filepath = self._output_format(data.get("video_data"))
            self._download_media(data.get("video_data"), filepath)
            self._save_json(data, self._expand_path(filepath + ".json"))
        except requests.exceptions.InvalidURL as e:
            self.logger.error(e)
            pass
        except ConnectionError as e:
            self.logger.error(e)
            pass
        except re.error as e:
            self.logger.error(e)
            pass
        except FileNotFoundError as e:
            self.logger.warning(e)
            pass
