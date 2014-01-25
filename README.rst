.. contents::

Introduction
============

Templates for OpenBSD stuff

**mr.bob** templates : http://mrbob.readthedocs.org/en/latest/

+ carp_iface : provide carp ifaces master and slave
+ carp_vlan : provide carp ifaces based on vlan master and slave


Installation
---------------

::
 
 easy_install bobtemplates.openbsd

or simply add bobtemplates.openbsd to your eggs zc.buildout section 

or with pip

:: 
 
 pip install bobtemplates.openbsd


Templates
------------


carp_iface
++++++++++++


carp_vlan
++++++++++


Tests
=====

bobtemplates.openbsd is continuously 

+ tested on Travis |travisstatus|_ 

+ coverage tracked on coveralls.io |coveralls|_.


.. |travisstatus| image:: https://api.travis-ci.org/jpcw/bobtemplates.openbsd.png?branch=master
.. _travisstatus:  http://travis-ci.org/jpcw/bobtemplates.openbsd


.. |coveralls| image:: https://coveralls.io/repos/jpcw/bobtemplates.openbsd/badge.png
.. _coveralls: https://coveralls.io/r/jpcw/bobtemplates.openbsd

