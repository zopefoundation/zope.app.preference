##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Tests for the Preferences System

$Id$
"""
from zope.app.testing import setup, functional
from zope.component import testing
import doctest
import unittest
import zope.app.preference.testing


def setUp(test):
    testing.setUp(test)
    setup.setUpTestAsModule(test, 'zope.app.preference.README')


def ftest_setUp(test):
    setup.setUpTestAsModule(test, 'zope.app.preference.zmi')


def tearDown(test):
    testing.tearDown(test)
    setup.tearDownTestAsModule(test)


def test_suite():
    browser_tests = functional.FunctionalDocFileSuite(
        'zmi.txt', setUp=ftest_setUp, tearDown=tearDown)
    browser_tests.layer = zope.app.preference.testing.PreferencesLayer

    return unittest.TestSuite((
        doctest.DocFileSuite('README.txt',
                             setUp=setUp, tearDown=tearDown,
                             optionflags=doctest.NORMALIZE_WHITESPACE),
        browser_tests,
        ))
