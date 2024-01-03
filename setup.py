"""Rachiopy setup script."""
from setuptools import find_packages, setup
from datetime import datetime

NOW = datetime.now().strftime("%m%d%Y%H%M%S")

VERSION = f"1.0.4-dev{NOW}"

GITHUB_USERNAME = "rfverbruggen"
GITHUB_REPOSITORY = "rachiopy"

GITHUB_PATH = f"{GITHUB_USERNAME}/{GITHUB_REPOSITORY}"
GITHUB_URL = f"https://github.com/{GITHUB_PATH}"

DOWNLOAD_URL = f"{GITHUB_URL}/archive/{VERSION}.tar.gz"
PROJECT_URLS = {"Bug Reports": f"{GITHUB_URL}/issues"}

PACKAGES = find_packages(exclude=["tests", "tests.*"])

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="RachioPy",
    version=VERSION,
    author="Robbert Verbruggen",
    author_email="rfverbruggen@icloud.com",
    packages=PACKAGES,
    install_requires=["requests"],
    url=GITHUB_URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    license="MIT",
    description="A Python module for the Rachio API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    platforms="Cross Platform",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
    ],
)
