"""Setup script."""

import setuptools

from downloader.settings import Config

with open('README.md') as file:
    long_description = file.read()

with open('requirements.txt') as file:
    requirements = [line.strip() for line in file]


setuptools.setup(
    name='cedl',
    version=Config.version,
    author='Alexander Potts',
    author_email='dev@jakkso.com',
    description='Chrome Extension Downloader',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jakkso/cedl',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points={"console_scripts": ["cedl = downloader.__main__:cedl"]},
    classifiers=(
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities"
    ),
)
