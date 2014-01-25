#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Render bobtemplates.jpcw hooks.
"""

__docformat__ = 'restructuredtext en'


#import os
from IPy import IP
from mrbob.bobexceptions import ValidationError


def within_intervall(str_value, name, lower_bound=1, upper_bound=255):
    """Check if int(answer) withoin intervall."""
    answer = str_value.strip()
    try:
        value = int(answer)
        if value not in range(lower_bound, upper_bound + 1):
            raise ValidationError("{0} Acceptable values for {1} are from {2} to {3}".format(answer, name, lower_bound, upper_bound))

    except ValidationError as e:
        raise(e)

    except:
        raise ValidationError("{0} is not a valid number".format(answer))

    return answer


def is_a_network_address(address):
    """Check if address is a network address."""
    try:
        net = IP(address)
        return bool(net)
    except:
        return False


def post_ask_q_carp_iface_cidr(configurator, question, answer):
    """Check subnet answer."""
    answer = answer.strip()
    net_vars = {}
    subnet = None

    try:
        if answer.count('/') != 1:
            raise ValidationError("'{0}' Plz input a cidr subnet notation here".format(answer))
        ip, netmask = answer.split('/')
        subnet = IP(answer, make_net=True)
        if netmask not in ['32', '128']:
            # we accept network ip only with /32 or /128
            if is_a_network_address(answer):
                raise ValidationError("'{0}': oO you provided a network address, within not in [/32 or /128] !".format(answer))
        net_vars['net'] = str(subnet.net())
        net_vars['netmask'] = str(subnet.netmask())
        net_vars['broadcast'] = str(subnet.broadcast())
        net_vars['ip'] = ip
        if netmask not in ['32', '128', '31', '127']:
            # we accept broadcast ip only with /32, /128, /31, /127
            if net_vars['ip'] == net_vars['broadcast']:
                raise ValidationError("'{0}': oO you provided a broadcast ip within not in [/32, /128, /31, /127]".format(answer))

    except ValidationError as e:
        raise(e)

    except:
        raise ValidationError("'{0}' is not a valid cidr ip".format(answer))

    configurator.variables.update(net_vars)
    return answer


def post_ask_q_carp_iface_vhid(configurator, question, answer):
    """Check vhid answer."""
    return within_intervall(answer, 'vhid')


def post_ask_q_carp_iface_advskew(configurator, question, answer):
    """Check advskew answer."""
    return within_intervall(answer, 'advskew', 1, 254)


def post_ask_q_carp_iface_description(configurator, question, answer):
    """Check description answer."""
    return answer.strip()[:48]


def carp_iface_pre_render(configurator):
    """pre render stuff."""
#    other_vars = {'year': date.today().year}
#    configurator.variables.update(other_vars)


def carp_iface_post_render(configurator):
    """post render stuff."""
#    clean_gpl(configurator)
#

# vim:set et sts=4 ts=4 tw=80:
