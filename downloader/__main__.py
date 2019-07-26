"""Create entry-point."""
from downloader import downloader


def cedl():
    """Create main routine."""
    downloader.run()


if __name__ == "__main__":
    cedl()
