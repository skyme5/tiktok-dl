"""Schema Validator for TikTok Video JSON."""
from jsonschema import validate
from jsonschema import ValidationError
from loguru import logger

from tiktok_dl.schema import schemas


class AwemeValidator:
    """Validate Schema for TikTok Video JSON."""

    def __init__(self):
        """Initialize schemas."""
        self.schemas = schemas()

    def validate(self, json_data: dict):
        """Validate json_data.

        This will try validating from collection of schema.

        Args:
            str (dict): json data to validate.

        Returns:
            bool: True If Scheme validation was a success.
            str : Version of the Schema that was validated.
        """
        for json_schema in self.schemas.reverse():
            try:
                validate(instance=json_data, schema=json_schema.get("SCHEMA"))
                logger.debug(
                    "Schema Validation success with " + json_schema.get("VERSION")
                )

                return (True, json_schema.get("VERSION"))
            except ValidationError as e:
                pass
        logger.warning("No valid schema exists for given json data")

        return (False, None)
