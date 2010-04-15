##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
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
from zope.app.testing import setup
from zope.component import testing
import doctest
import unittest

def setUp(test):
    testing.setUp(test)
    setup.setUpTestAsModule(test, 'zope.app.preference.README')

def tearDown(test):
    testing.tearDown(test)
    setup.tearDownTestAsModule(test)

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite('README.txt',
                             setUp=setUp, tearDown=tearDown,
                             optionflags=doctest.NORMALIZE_WHITESPACE),
        ))
