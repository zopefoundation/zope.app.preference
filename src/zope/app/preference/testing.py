##############################################################################
#
# Copyright (c) 2007 Zope Corporation and Contributors.
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
"""zope.app.preferences common test related classes/functions/objects.

$Id$
"""

__docformat__ = "reStructuredText"

import os
from zope.app.testing.functional import ZCMLLayer

PreferencesLayer = ZCMLLayer(
    os.path.join(os.path.split(__file__)[0], 'ftesting.zcml'),
    __name__, 'PreferencesLayer', allow_teardown=True)
