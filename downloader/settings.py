"""Contain configuration class."""
import pathlib


class Config:
    """Contain configuration values.

    Change `chrome_version` to match your version of chrome
    download_directory defaults to ~/bin/chrome-extensions, change if you wish
    """

    chrome_version = "70.0"
    download_directory = pathlib.Path().home() / "bin" / "chrome-extensions"
    version = '0.1.3'
