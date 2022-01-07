"""Extractor for extracting data from JSON."""
from tiktok_dl.extractors.extractor_20200623 import Extractor20200623


class ExtractorError(Exception):
    """No Extractor found.

    Args:
        Exception (Exception): If no Extractor found.
    """

    pass


class Extractor:
    """Extract TikTok Video JSON."""

    def extract(self, json_data: dict, version: str):
        """Extract data from json_data with json schema version.

        Args:
            json_data (dict): Data to be extracted from.
            version (str): Version of the json schema to use.

        Returns:
            dict: Extracted json data.
        """
        for extractor in [Extractor20200623()]:
            if extractor.__class__.version() == version:
                return (version, extractor.__class__.extract(json_data))

        raise ExtractorError("Unable to extract from json_data")
