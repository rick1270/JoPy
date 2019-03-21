#!/usr/bin/env python
# Package setup/installation and metadata for JoPy

import setuptools

REQUIRED = [
    'pandas',
    'matplotlib',
    'geopy',
    'urllib3',
    'pillow'
]

with open('README.md') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="JoPy",
    version="0.0.1",
    author="Rick Clayton",
    description="A collection of tools for using plotting with google maps",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/rick1270/JoPy",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)