##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
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
"""Setup for zope.app.preference package

$Id$
"""

import os

from setuptools import setup, find_packages

setup(name = 'zope.app.preference',
      version = '3.4.0b1',
      url = 'http://svn.zope.org/zope.app.preference',
      license = 'ZPL 2.1',
      description = 'Zope app.preference',
      author = 'Zope Corporation and Contributors',
      author_email = 'zope3-dev@zope.org',
      long_description = "",

      packages = find_packages('src'),
      package_dir = {'': 'src'},

      namespace_packages = ['zope', 'zope.app'],
      install_requires = ['setuptools',
                          'ZODB3',
                          'zope.annotation',
                          'zope.app.basicskin',
                          'zope.app.component',
                          'zope.app.container',
                          'zope.app.form',
                          'zope.app.pagetemplate',
                          'zope.app.preference',
                          'zope.app.testing',
                          'zope.app.tree',
                          'zope.app.zapi',
                          'zope.component',
                          'zope.configuration',
                          'zope.i18n',
                          'zope.i18nmessageid',
                          'zope.interface',
                          'zope.location',
                          'zope.schema',
                          'zope.security',
                          'zope.testing',
                          'zope.traversing',
                          ],
      include_package_data = True,

      zip_safe = False,
      )
