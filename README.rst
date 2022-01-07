==================================
tiktok-dl: TikTok Video Downloader
==================================


.. image:: https://img.shields.io/pypi/v/tiktok_dl.svg
        :target: https://pypi.python.org/pypi/tiktok_dl

.. image:: https://img.shields.io/travis/skyme5/tiktok_dl.svg
        :target: https://travis-ci.com/skyme5/tiktok_dl

.. image:: https://readthedocs.org/projects/tiktok-dl/badge/?version=latest
        :target: https://tiktok-dl.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/skyme5/tiktok_dl/shield.svg
     :target: https://pyup.io/repos/github/skyme5/tiktok_dl/
     :alt: Updates


Usage
-----

..  code-block:: text

    usage: cli.py [-h] [-V] [--download-archive DOWNLOAD_ARCHIVE] [-d]                  [-p CONCURRENT_COUNT] [-a FILENAME] [-o OUTPUT_TEMPLATE] [-w]                  [--write-description] [--no-write-json] [-P DIRECTORY_PREFIX]                  [--write-thumbnail] [-q] [--no-warnings] [-s] [--skip-download]                  [-g] [-e] [--get-id] [--get-thumbnail] [--get-description]                  [--get-duration] [--get-filename] [-j] [--print-json] [-v]                  [--no-check-certificate] [--sleep-interval SLEEP_INTERVAL]                  [--max-sleep-interval MAX_SLEEP_INTERVAL]                  [URL [URL ...]]        TikTok Video downloader        positional arguments:      URL                   URL of the video        optional arguments:      -h, --help            show this help message and exit      -V, --version         Print program version and exit        Video Selection:      --download-archive DOWNLOAD_ARCHIVE                            Download only videos not listed in the archive file.                            Record the IDs of all downloaded videos in it.        Parallel Download:      -d, --daemon          Run as daemon.      -p CONCURRENT_COUNT, --concurrent-count CONCURRENT_COUNT                            Download videos in parallel.        Filesystem Options:      -a FILENAME, --batch-file FILENAME                            File containing URLs to download ('-' for stdin), one                            URL per line. Lines starting with '#', ';' or ']' are                            considered as comments and ignored.      -o OUTPUT_TEMPLATE, --output-template OUTPUT_TEMPLATE                            Output filename template, see the "OUTPUT TEMPLATE"                            for all the info.      -w, --no-overwrite    Do not overwrite files      --write-description   Write video description to a .description file.      --no-write-json       Write video metadata to a .json file.      -P DIRECTORY_PREFIX, --directory-prefix DIRECTORY_PREFIX                            Directory prefix.        Thumbnail images:      --write-thumbnail     Write thumbnail image to disk.        Verbosity / Simulation Options::      -q, --quiet           Activate quiet mode.      --no-warnings         Ignore warnings.      -s, --simulate        Do not download the video and do not write anything to                            disk.      --skip-download       Do not download the video.      -g, --get-url         Simulate, quiet but print URL.      -e, --get-title       Simulate, quiet but print title.      --get-id              Simulate, quiet but print id.      --get-thumbnail       Simulate, quiet but print thumbnail URL.      --get-description     Simulate, quiet but print video description.      --get-duration        Simulate, quiet but print video length.      --get-filename        Simulate, quiet but print output filename.      -j, --dump-json       Simulate, quiet but print JSON information. See the                            "OUTPUT TEMPLATE" for a description of available keys.      --print-json          Be quiet and print the video information as JSON                            (video is still being downloaded).      -v, --verbose         Print various debugging information.        Workarounds:      --no-check-certificate                            Suppress HTTPS certificate validation.      --sleep-interval SLEEP_INTERVAL                            Number of seconds to sleep before each download when                            used alone or a lower bound of a range for randomized                            sleep before each download (minimum possible number of                            seconds to sleep) when used along with --max-sleep-                            interval.      --max-sleep-interval MAX_SLEEP_INTERVAL                            Upper bound of a range for randomized sleep before                            each download (maximum possible number of seconds to                            sleep). Must only be used along with --min-sleep-                            interval.


* Free software: MIT license
* Documentation: https://tiktok-dl.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
