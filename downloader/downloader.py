"""Contain Utility script to download a chrome extension."""
import re

import click
import requests

from downloader.settings import Config

PATTERN = re.compile(r"/detail/.*/(.*)\?")
BACKUP_PATTERN = re.compile(r"/detail/.*/(.*)\??")

if not Config.download_directory.exists():
    Config.download_directory.mkdir(parents=True)


@click.command()
@click.argument("url")
@click.argument("filename")
def run(url: str, filename: str) -> None:
    """Download the chrome extension located at url.

    In order of arguments, url goes first, then filename.

    :param url: URL to chrome webstore extension.\n
    :param filename: .crx filename.  Name it something recognizable.

    To install the downloaded extension, open chrome://extensions, then drag the
    downloaded file onto the page.
    """
    try:
        extension_id = extract_extension_id(url)
        template_url = (
            f"https://clients2.google.com/service/update2/crx?response=redirect"
            f"&acceptformat=crx2,crx3&prodversion={Config.chrome_version}&x=id%3D{extension_id}%26"
            f"installsource%3Dondemand%26uc"
        )
        resp = requests.get(template_url)
        if resp.ok:
            with open(str(Config.download_directory / f"{filename}.crx"), "wb") as file:
                file.write(resp.content)
            click.echo("Downloaded successfully")
        else:
            click.echo("Failed to download: bad request")
    except RuntimeError as err:
        print(err)


def extract_extension_id(url: str) -> str:
    """Return extracted extension ID from chrome web store url

    :param url:
    :return: extension id.
    """
    extension_id = PATTERN.search(url)
    if extension_id:
        return extension_id.groups()[0]
    elif '?' not in url:
        extension_id = BACKUP_PATTERN.search(url)
        if extension_id:
            return extension_id.groups()[0]
    raise RuntimeError("Failed to extract extension ID from url!")
