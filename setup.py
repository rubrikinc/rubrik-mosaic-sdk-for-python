#! /usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rubrik_mosaic",
    version="0.0.1",
    author="Rubrik Build",
    description="A Python package for interacting with the Rubrik Mosaic API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rubrik-devops/rubrik-sdk-for-python",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6"
    ],
    install_requires=[
        'requests >= 2.18.4',
    ],
    tests_require=[
        'pytest'
    ],
    zip_safe=True,
)
