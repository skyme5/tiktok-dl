"""Console script for tiktok_dl."""
import os
import sys

from loguru import logger

from tiktok_dl.options import options_parser
from tiktok_dl.tiktok_dl import TikTokDownloader


def main():
    """Console script for tiktok_dl."""
    parser = options_parser()
    args = parser.parse_args()

    if len(args.urls) == 0 and args.batch_file is None:
        parser.error("URL or file containing list of URLs (--batch-file) is required.")

    if args.batch_file is not None and os.path.isfile(args.batch_file):
        with open(args.batch_file, "r") as f:
            for url in f.read().split("\n"):
                if len(url.strip()) > 0:
                    args.urls.append(url.strip())

    logger.info("Downloading {} urls", len(args.urls))

    tiktok = TikTokDownloader(args)
    tiktok.process_urls()

    print("Arguments: " + str(args))
    print("Replace this message by putting your code into " "tiktok_dl.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
