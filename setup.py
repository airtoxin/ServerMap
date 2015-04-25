#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, absolute_import
from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="ServerMap",
    version="0.1.0dev",
    description="Resource monitoring tool for servers.",
    long_description=long_description,
    author="airtoxin",
    author_email="airtoxin@icloud.com",
    url="https://github.com/airtoxin/servermap",
    packages=find_packages(exclude=["docs"]),
    include_package_data=True,
    install_requires=[
        "Fabric",
        "Flask",
        "plugin-loader",
        "apscheduler"
    ],
    tests_require=["nose"],
    license="MIT",
    keywords="",
    zip_safe=False,
    classifiers=[
        "development Status :: 1 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ]
)
