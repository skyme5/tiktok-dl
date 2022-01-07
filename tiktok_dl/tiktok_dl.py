"""Main module."""
from tiktok_dl.downloader import Downloader
from tiktok_dl.extractors.extractor import Extractor
from tiktok_dl.logger import Logger
from tiktok_dl.validator import AwemeValidator


class TikTokDownloader:
    """TikTok Downloader Class."""

    def __init__(self, options):
        """Initialize validator, extractor, logger and downloader.

        Args:
            options (dict): Dictionary of command-line options.
        """
        self.options = options
        self.validator = AwemeValidator()
        self.extractor = Extractor()
        self.logger = Logger(
            no_warnings=self.options.no_warnings,
            quiet=self.options.quiet,
            verbose=self.options.verbose,
        )
        self.downloader = Downloader(
            validator=self.validator,
            extractor=self.extractor,
            logger=self.logger,
            directory_prefix=self.options.directory_prefix,
            dump_json=self.options.dump_json,
            max_sleep_interval=self.options.max_sleep_interval,
            no_check_certificate=self.options.no_check_certificate,
            no_overwrite=self.options.no_overwrite,
            no_write_json=self.options.no_write_json,
            output_template=self.options.output_template,
            print_json=self.options.print_json,
            simulate=self.options.simulate,
            skip_download=self.options.skip_download,
            sleep_interval=self.options.sleep_interval,
            write_description=self.options.write_description,
            write_thumbnail=self.options.write_thumbnail,
        )

    def download(self, url):
        def queue(url):
            pass

        queue(url)

    def process_urls(self):
        for url in self.options.urls:
            self.download(url)
