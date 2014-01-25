#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Doc here.
"""

__docformat__ = 'restructuredtext en'

#import os
#import shutil
#import tempfile
#
#from datetime import date
from unittest import TestCase


class DummyConfigurator(object):
    def __init__(self,
                 defaults=None,
                 bobconfig=None,
                 templateconfig=None,
                 variables=None,
                 quiet=False):
        self.defaults = defaults or {}
        self.bobconfig = bobconfig or {}
        self.variables = variables or {}
        self.quiet = quiet
        self.templateconfig = templateconfig or {}

#
#class Basic_NamespaceTest(TestCase):
#
#    def setUp(self):
#        self.target_dir = tempfile.mkdtemp()
#
#    def tearDown(self):
#        shutil.rmtree(self.target_dir)
#
#    def call_FUT(self, *args, **kw):
#        from mrbob.configurator import Configurator
#        return Configurator(*args, **kw)
#
#    def test_ns_pkg(self):
#        from ..hooks import basicnamespace_pre_pkg_ns
#        from ..hooks import basicnamespace_pre_pkg_project
#        configurator = self.call_FUT('bobtemplates.jpcw:basic_namespace',
#                                     'mynamespace.mypkg', {})
#        self.assertEquals(configurator.questions[0].default, None)
#        basicnamespace_pre_pkg_ns(configurator, configurator.questions[0])
#        self.assertEquals(configurator.questions[0].default, 'mynamespace')
#
#        self.assertEquals(configurator.questions[1].default, None)
#        basicnamespace_pre_pkg_project(configurator, configurator.questions[1])
#        self.assertEquals(configurator.questions[1].default, 'mypkg')
#
#    def test_basic_namespace_pre_render(self):
#        from ..hooks import basic_namespace_pre_render
#        configurator = self.call_FUT('bobtemplates.jpcw:basic_namespace',
#                                     'mynamespace.mypkg', {})
#        basic_namespace_pre_render(configurator)
#        self.assertEquals(configurator.variables['year'], date.today().year)
#


class ToolsTest(TestCase):

    def test_within_intervall(self):
        from mrbob.bobexceptions import ValidationError
        from ..hooks import within_intervall
        self.assertRaises(ValidationError, within_intervall, 'O', 'test')
        self.assertRaises(ValidationError, within_intervall, '256', 'test')
        self.assertEquals(within_intervall('200', 'test'), '200')

    def test_is_a_network_address(self):
        from ..hooks import is_a_network_address
        self.assertTrue(is_a_network_address('192.168.0.1/32'))
        self.assertFalse(is_a_network_address('192.168.0.1/31'))


class Post_ask_q_carp_iface_cidrTest(TestCase):

    def call_FUT(self, answer, configurator=None, question=None):
        from ..hooks import post_ask_q_carp_iface_cidr
        return post_ask_q_carp_iface_cidr(DummyConfigurator(), question, answer)

    def test_post_ask_q_carp_iface_cidr(self):
        from mrbob.bobexceptions import ValidationError
        self.assertRaises(ValidationError, self.call_FUT, 'test')
        self.assertRaises(ValidationError, self.call_FUT, 'test/32')
        self.assertRaises(ValidationError, self.call_FUT, '192.168.0.3/30')
        self.assertRaises(ValidationError, self.call_FUT, '192.168.0.0/31')
        self.assertEquals(self.call_FUT('192.168.0.1/30'), '192.168.0.1/30')


class Post_ask_q_carp_iface_vhidTest(TestCase):

    def call_FUT(self, answer, configurator=None, question=None):
        from ..hooks import post_ask_q_carp_iface_vhid
        return post_ask_q_carp_iface_vhid(DummyConfigurator(), question, answer)

    def test_post_ask_q_carp_iface_vhid(self):
        from mrbob.bobexceptions import ValidationError
        self.assertRaises(ValidationError, self.call_FUT, 'test')
        self.assertRaises(ValidationError, self.call_FUT, '0')
        self.assertEquals(self.call_FUT('255'), '255')


class Post_ask_q_carp_iface_advskewTest(TestCase):

    def call_FUT(self, answer, configurator=None, question=None):
        from ..hooks import post_ask_q_carp_iface_advskew
        return post_ask_q_carp_iface_advskew(DummyConfigurator(), question, answer)

    def test_post_ask_q_carp_iface_advskew(self):
        from mrbob.bobexceptions import ValidationError
        self.assertRaises(ValidationError, self.call_FUT, 'test')
        self.assertRaises(ValidationError, self.call_FUT, '0')
        self.assertRaises(ValidationError, self.call_FUT, '255')
        self.assertEquals(self.call_FUT('254'), '254')


class Post_ask_q_carp_iface_descriptionTest(TestCase):

    def call_FUT(self, answer, configurator=None, question=None):
        from ..hooks import post_ask_q_carp_iface_description
        return post_ask_q_carp_iface_description(DummyConfigurator(), question, answer)

    def test_post_ask_q_carp_iface_description(self):
        from string import ascii_letters
        self.assertEquals(len(self.call_FUT(ascii_letters)), 48)
        self.assertEquals(self.call_FUT(' test '), 'test')


#class render_structureTest(TestCase):
#
#    def setUp(self):
#        import bobtemplates.openbsd
#        self.fs_tempdir = tempfile.mkdtemp()
#        base_path = os.path.dirname(bobtemplates.jpcw.__file__)
#        self.fs_templates = base_path
#
#    def tearDown(self):
#        shutil.rmtree(self.fs_tempdir)
#
#    def call_FUT(self, template, variables, output_dir=None, verbose=True,
#                 renderer=None, ignored_files=[]):
#        from mrbob.rendering import render_structure
#        from mrbob.rendering import jinja2_renderer
#
#        if output_dir is None:
#            output_dir = self.fs_tempdir
#
#        if renderer is None:
#            renderer = jinja2_renderer
#
#        render_structure(
#            template,
#            output_dir,
#            variables,
#            verbose,
#            renderer,
#            ignored_files,
#        )
#
#    def test_clean_gpl(self):
#
#        from ..hooks import basic_namespace_post_render
#        tpl_vars = {'pkg_license': 'BSD', 'pkg_ns': 'mytruc',
#                    'pkg_keywords': 'Python', 'pkg_author_name': 'me',
#                    'pkg_author_email': 'me@.tld', 'pkg_url': 'http://.tld',
#                    'pkg_zipsafe': 'false', 'year': 2013, 'pkg_project': 'my',
#                    'pkg_description': 'testing my templates'}
#
#        self.call_FUT(os.path.join(self.fs_templates, 'basic_namespace'),
#                      tpl_vars)
#        self.assertTrue(os.path.exists('%s/%s' % (self.fs_tempdir,
#                                       'docs/LICENSE.txt')))
#        self.assertTrue(os.path.exists('%s/%s' % (self.fs_tempdir,
#                                       'docs/LICENSE.gpl')))
#        configurator = DummyConfigurator(variables=tpl_vars)
#        configurator.target_directory = self.fs_tempdir
#        basic_namespace_post_render(configurator)
#        self.assertFalse(os.path.exists('%s/%s' % (self.fs_tempdir,
#                                        'docs/LICENSE.gpl')))
#

# vim:set et sts=4 ts=4 tw=80:
