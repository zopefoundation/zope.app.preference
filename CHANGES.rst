=========
 CHANGES
=========

4.1.0 (2022-08-05)
==================

- Add support for Python 3.7, 3.8, 3.9, 3.10.

- Drop support for Python 3.4.


4.0.0 (2017-05-17)
==================

- Add support for Python 3.4, 3.5, 3.6 and PyPy.

- Removed test dependency on ``zope.app.zcmlfiles`` and
  ``zope.app.renderer``, among others. ``zope.app.renderer`` is still
  required at runtime.

- Broke test dependency on ``zope.app.testing`` by using
  ``zope.app.wsgi.testlayer``.


3.8.1 (2010-06-15)
==================

- Fixed BBB imports which pointed to a not existing `zope.preferences`
  package.


3.8.0 (2010-06-12)
==================

- Depend on split out `zope.preference`.


3.7.0 (2010-06-11)
==================

- Added HTML labels to ZMI forms.

- Removed `edit.pt` as it seems to be unused.

- Added tests for the ZMI views.


3.6.0 (2009-02-01)
==================

- Use ``zope.container`` instead of ``zope.app.container``.


3.5.0 (2009-01-17)
==================

- Got rid of ``zope.app.zapi`` dependency, replacing its uses with direct
  imports from original places.

- Change mailing address from zope3-dev to zope-dev, as the first one
  is retired now.

- Fix tests for python 2.6.

- Remove zpkg stuff and zcml include files for
  old mkzopeinstance-based instances.


3.4.1 (2007-10-30)
==================

- Avoid deprecation warnings for ``ZopeMessageFactory``.


3.4.0 (2007-10-25)
==================

- Initial release independent of the main Zope tree.
