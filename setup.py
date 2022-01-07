#!/usr/bin/env python
"""The setup script."""
from setuptools import find_packages
from setuptools import setup

from tiktok_dl.version import __version__

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    name="tiktok-dl",
    version=__version__,
    author="Aakash Gajjar",
    author_email="skyqutip@gmail.com",
    url="https://github.com/skyme5/tiktok-dl",
    description="TikTok Video Downloader",
    long_description=readme + "\n\n" + history,
    entry_points={"console_scripts": ["tiktok-dl=tiktok_dl.cli:main",],},
    include_package_data=True,
    packages=find_packages(include=["tiktok_dl", "tiktok_dl.*"]),
    install_requires=requirements,
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    keywords="tiktok-dl",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license="MIT license",
    zip_safe=False,
)
