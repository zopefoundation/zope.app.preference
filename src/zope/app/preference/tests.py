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
import doctest
import zope.app.preference.testing
import zope.component.testing
import zope.testing.module


def setUp(test):
    zope.testing.module.setUp(test, 'zope.app.preference.README')


def tearDown(test):
    zope.component.testing.tearDown(test)
    zope.testing.module.tearDown(test)


def test_suite():
    suite = doctest.DocFileSuite(
        'README.txt', setUp=setUp, tearDown=tearDown)
    suite.layer = zope.app.preference.testing.PreferencesLayer
    return suite
