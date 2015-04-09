#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import ok_, eq_
from servermap.cmdline import main

class CmdlineTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_main(self):
        eq_(main(), None)
