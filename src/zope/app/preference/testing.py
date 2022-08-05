##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
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
"""zope.app.preference common test related classes/functions/objects.

"""

from zope.app.wsgi.testlayer import BrowserLayer
from zope.testbrowser.wsgi import TestBrowserLayer

import zope.app.preference


class _PreferencesLayer(TestBrowserLayer,
                        BrowserLayer):
    pass


PreferencesLayer = _PreferencesLayer(zope.app.preference)
