# Chrome Extension Downloader (CEDL)

This is a simple utility program to download extensions from the Chrome WebStore.

## Installation
    pip install cedl


## Usage
    cedl [url] [name]

Where `url` is the WebStore url for the extension that you want to download and `name` is the filename you want for the downloaded extension.

Downloaded extensions are placed in `$HOME/bin/chrome-extensions`   

To install the downloaded extension, open `chrome://extensions` in chrome, then drag the downloaded file onto the page.

#### License

MIT