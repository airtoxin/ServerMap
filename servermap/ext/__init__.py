#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def setup():
    from ..exthook import ExtensionImporter
    importer = ExtensionImporter(['cartographer%s', 'cartographerext.%s'], __name__)
    importer.install()


setup()
del setup
