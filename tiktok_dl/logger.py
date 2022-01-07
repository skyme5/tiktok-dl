"""Logger Class."""
from loguru import logger


class Logger:
    """Wrapper for logger."""

    def __init__(
        self, no_warnings=False, quiet=False, verbose=True,
    ):
        """Set class options.

    Args:
        no_warnings (bool, optional): Do not log any warnings. Defaults to False.
        quiet (bool, optional): Do not print anything. Defaults to False.
        verbose (bool, optional): Be verbose. Defaults to True.
    """

        self.no_warnings = no_warnings
        self.quiet = quiet
        self.verbose = verbose

    def debug(self, *args):
        if self.verbose:
            logger.debug(*args)

    def info(self, *args):
        if self.verbose:
            logger.info(*args)

    def warning(self, *args):
        if not self.no_warnings or not self.quiet:
            logger.warning(*args)

    def error(self, *args):
        if self.verbose or not self.quiet:
            logger.error(*args)
