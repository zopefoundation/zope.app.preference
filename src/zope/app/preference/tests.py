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

"""
import doctest
import importlib
import unittest

import docutils.core

import zope.component.testing
import zope.testing.module
# Previously from zope.app.renderer
from zope.component.interfaces import IFactory
from zope.interface import Interface
from zope.interface import directlyProvides
from zope.interface import implementer
from zope.publisher.browser import BrowserView

import zope.app.preference.testing


class ISource(Interface):
    """Simple base interface for all possible Wiki Page Source types."""


class IReStructuredTextSource(ISource):
    """Marker interface for a restructured text source. Note that an
    implementation of this interface should always derive from unicode or
    behave like a unicode class."""


try:
    text_type = unicode
except NameError:
    text_type = str


class Source(text_type):
    __provides__ = None


@implementer(IFactory)
class SourceFactory(object):
    """Creates an ISource object."""

    def __init__(self, iface, title='', description=''):
        self._iface = iface
        self.title = title
        self.description = description

    def __call__(self, ustr):
        source = Source(ustr)
        directlyProvides(source, self._iface)
        return source


ReStructuredTextSourceFactory = SourceFactory(
    IReStructuredTextSource, u"ReStructured Text (ReST)",
    u"ReStructured Text (ReST) Source")


class _ReStructuredTextToHTMLRenderer(BrowserView):
    r"""An Adapter to convert from Restructured Text to HTML.

    Examples::

      >>> from zope.publisher.browser import TestRequest
      >>> source = u'''
      ... This is source.
      ...
      ... Header 3
      ... --------
      ... This is more source.
      ... '''
      >>> renderer = _ReStructuredTextToHTMLRenderer(source, TestRequest())
      >>> print(renderer.render().strip())
      <p>This is source.</p>
      <div class="section" id="header-3">
      <h3>Header 3</h3>
      <p>This is more source.</p>
      </div>
    """

    # Lifted from zope.app.renderers.rest

    def render(self, settings_overrides={}):
        """See zope.app.interfaces.renderer.IHTMLRenderer

        Let's make sure that inputted unicode stays as unicode:

        >>> renderer = _ReStructuredTextToHTMLRenderer(u'b\xc3h', None)
        >>> output = renderer.render()
        >>> isinstance(output, bytes)
        False


        >>> text = u'''
        ... =========
        ... Heading 1
        ... =========
        ...
        ... hello world
        ...
        ... Heading 2
        ... ========='''
        >>> overrides = {'initial_header_level': 2,
        ...              'doctitle_xform': 0 }
        >>> renderer = _ReStructuredTextToHTMLRenderer(text, None)
        >>> print(renderer.render(overrides))
        <div class="section" id="heading-1">
        <h2>Heading 1</h2>
        <p>hello world</p>
        <div class="section" id="heading-2">
        <h3>Heading 2</h3>
        </div>
        </div>
        <BLANKLINE>
        """
        # default settings for the renderer
        overrides = {
            'halt_level': 6,
            'input_encoding': 'unicode',
            'output_encoding': 'unicode',
            'initial_header_level': 3,
        }
        overrides.update(settings_overrides)
        parts = docutils.core.publish_parts(
            self.context,
            writer_name='html',
            settings_overrides=overrides,
        )
        return u''.join(
            (parts['body_pre_docinfo'], parts['docinfo'], parts['body']))


def _make_import_test(mod_name, attrname):
    def test(self):
        mod = importlib.import_module('zope.app.preference.' + mod_name)
        self.assertIsNotNone(getattr(mod, attrname, None),
                             str(mod) + ' has no ' + attrname)

    return test


class TestBWCImports(unittest.TestCase):

    for mod_name, attrname in (
            ('default', 'DefaultPreferenceGroup'),
            ('interfaces', 'IPreferenceGroup'),
            ('metaconfigure', 'preferenceGroup'),
            ('metadirectives', 'IPreferenceGroupDirective'),
            ('preference', 'PreferenceGroup'),
    ):
        locals()['test_' + mod_name] = _make_import_test(mod_name, attrname)


def setUp(test):
    zope.testing.module.setUp(test, 'zope.app.preference.README')


def tearDown(test):
    zope.component.testing.tearDown(test)
    zope.testing.module.tearDown(test)


def test_suite():
    readme = doctest.DocFileSuite(
        'README.rst',
        setUp=setUp,
        tearDown=tearDown)
    readme.layer = zope.app.preference.testing.PreferencesLayer
    return unittest.TestSuite((
        readme,
        unittest.defaultTestLoader.loadTestsFromName(__name__),
    ))
