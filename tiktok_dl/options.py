"""Command-line Options for tiktok_dl."""
import argparse

from tiktok_dl.version import __version__


def options_parser():
    """Parser Command-line Options."""
    parser = argparse.ArgumentParser(description="TikTok Video downloader",)

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=__version__,
        help="Print program version and exit",
    )

    parser.add_argument(
        "urls", metavar="URL", nargs="*", type=str, help="URL of the video"
    )

    video_selection_group = parser.add_argument_group("Video Selection")
    video_selection_group.add_argument(
        "-a",
        "--download-archive",
        metavar="DOWNLOAD_ARCHIVE",
        type=str,
        default=None,
        help="Download only videos not listed in the archive file. "
        "Record the IDs of all downloaded videos in it.",
    )

    parallel_download_group = parser.add_argument_group("Parallel Download")
    parallel_download_group.add_argument(
        "-d", "--daemon", action="store_true", dest="daemon", help="Run as daemon.",
    )
    parallel_download_group.add_argument(
        "-j",
        "--concurrent-count",
        metavar="CONCURRENT_COUNT",
        type=int,
        default=2,
        help="Download videos in parallel.",
    )

    filesystem_group = parser.add_argument_group("Filesystem Options")
    filesystem_group.add_argument(
        "-i",
        "--batch-file",
        metavar="FILENAME",
        type=str,
        default=None,
        help="File containing URLs to download ('-' for stdin), one URL per line. "
        "Lines starting with '#', ';' or ']' are considered as comments and ignored.",
    )
    filesystem_group.add_argument(
        "-o",
        "--output-template",
        metavar="OUTPUT_TEMPLATE",
        type=str,
        default="{Y}-{d}-{m}_{H}-{M}-{S} {id}_{user_id}",
        help='Output filename template, see the "OUTPUT TEMPLATE" for all the info.',
    )
    filesystem_group.add_argument(
        "-n",
        "--no-overwrite",
        action="store_true",
        default=False,
        help="Do not overwrite files",
    )
    filesystem_group.add_argument(
        "--write-description",
        action="store_true",
        help="Write video description to a .description file.",
    )
    filesystem_group.add_argument(
        "--no-write-json",
        action="store_true",
        default=False,
        help="Write video metadata to a .json file.",
    )
    filesystem_group.add_argument(
        "-P",
        "--directory-prefix",
        metavar="DIRECTORY_PREFIX",
        type=str,
        default=None,
        help="Directory prefix.",
    )

    thumbnail_group = parser.add_argument_group("Thumbnail images")
    thumbnail_group.add_argument(
        "--write-thumbnail",
        action="store_true",
        default=True,
        help="Write thumbnail image to disk.",
    )

    simulation_group = parser.add_argument_group("Verbosity / Simulation Options:")
    simulation_group.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        default=False,
        help="Activate quiet mode.",
    )
    simulation_group.add_argument(
        "--no-warnings", action="store_true", default=False, help="Ignore warnings.",
    )
    simulation_group.add_argument(
        "-s",
        "--simulate",
        action="store_true",
        default=False,
        help="Do not download the video and do not write anything to disk.",
    )
    simulation_group.add_argument(
        "--skip-download",
        action="store_true",
        default=False,
        help="Do not download the video.",
    )
    simulation_group.add_argument(
        "--dump-json",
        action="store_true",
        default=False,
        help="Simulate, quiet but print JSON information. "
        'See the "OUTPUT TEMPLATE" for a description of available keys.',
    )
    simulation_group.add_argument(
        "--print-json",
        action="store_true",
        default=False,
        help="Be quiet and print the video information as JSON (video is still being downloaded).",
    )
    simulation_group.add_argument(
        "-v",
        "--verbose",
        action="store_false",
        default=True,
        help="Print various debugging information.",
    )

    workarounds_group = parser.add_argument_group("Workarounds")
    workarounds_group.add_argument(
        "--no-check-certificate",
        action="store_true",
        default=False,
        help="Suppress HTTPS certificate validation.",
    )
    workarounds_group.add_argument(
        "--sleep-interval",
        metavar="SLEEP_INTERVAL",
        type=float,
        default=0.2,
        help="Number of seconds to sleep before each download.",
    )
    workarounds_group.add_argument(
        "--max-sleep-interval",
        metavar="MAX_SLEEP_INTERVAL",
        type=float,
        default=0,
        help="Maximum possible number of seconds to sleep.",
    )
    parser.set_defaults(
        batch_file=None,
        concurrent_count=1,
        daemon=False,
        directory_prefix=None,
        download_archive=None,
        dump_json=False,
        get_description=False,
        get_duration=False,
        get_filename=False,
        get_id=True,
        get_thumbnail=False,
        get_title=False,
        get_url=False,
        max_sleep_interval=0,
        no_check_certificate=False,
        no_overwrite=False,
        no_warnings=False,
        no_write_json=False,
        output_template="{Y}-{d}-{m}_{H}-{M}-{S} {id}_{user_id}",
        print_json=False,
        quiet=False,
        simulate=False,
        skip_download=False,
        sleep_interval=0.2,
        urls=[],
        verbose=True,
        write_description=False,
        write_thumbnail=True,
    )

    return parser
