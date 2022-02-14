from setuptools import setup

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="streamxml2json",
    version="1.0.0.2",
    packages=("streamxml2json",),
    url="https://github.com/rafaeelaudibert/streamxml2json",
    license="MIT",
    author="RafaAudibert",
    author_email="rafaeelaudibert@gmail.com",
    install_requires=(),
    tests_require=(),
    description=("Simple library to stream a huge XML file to a JSON file"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ),
)
