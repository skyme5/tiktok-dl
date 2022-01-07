"""Archive Manager for tiktok_dl."""


class ArchiveManager:
    """Manage Archive file containing ids of downloaded TikTok Videos."""

    def __init__(self, download_archive=None):
        """Initialize Archive Manager.

           1. Read archive list from disc.
           2. Open file object for archive list

        Args:
            download_archive (str, optional): File path of the local archive. Defaults to None.
        """
        self.archive_path = download_archive
        self.enable_archive = download_archive is not None
        self.archive_file = self._open()
        self.list = self._init_archive()

    def _open(self):
        """Open archive file for reading+writing."""
        if self.enable_archive:
            return open(self.archive_path, "r+", encoding="utf-8")
        return None

    def _init_archive(self):
        """Read local archive file."""
        return self.archive_file.read().strip().split("\n")

    def _update_archive(self, video_id: str):
        self.list.append(video_id)
        if self.enable_archive:
            self.archive_file.write("%s\n" % video_id)

    def recorded(self, video_id: str):
        """Check if the video_id exists in the Archive?.

        Args:
            video_id (str): id of the TikTok Video

        Returns:
            bool: True if exists in archive
        """
        return video_id in self.list

    def append(self, video_id: str):
        """Record video_id to the archive.

        Args:
            video_id (str): id of the TikTok Video
        """
        self._update_archive(video_id)

    def close(self):
        """Close Archive Manager."""
        if self.enable_archive:
            self.archive_file.close()
