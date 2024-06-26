#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_lag_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_lag_interfaces
version_added: 1.0.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
short_description: Manage link aggregation group (LAG) interface parameters
description:
  - This module manages attributes of link aggregation group (LAG) interfaces of
    devices running Enterprise SONiC Distribution by Dell Technologies.
author: Abirami N (@abirami-n)

options:
  config:
    description: A list of LAG configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - ID of the LAG.
        type: str
        required: True
      members:
        description:
          - The list of interfaces that are part of the group.
        type: dict
        suboptions:
          interfaces:
            description: The list of interfaces that are part of the group.
            type: list
            elements: dict
            suboptions:
              member:
                description:
                  - The interface name.
                type: str
      mode:
        description:
          - Specifies mode of the port-channel while creation.
        type: str
        choices:
          - static
          - lacp
  state:
    description:
      - The state that the configuration should be left in.
    type: str
    choices:
     - merged
     - replaced
     - overridden
     - deleted
    default: merged
"""
EXAMPLES = """
# Using merged
#
# Before state:
# -------------
#
# interface Eth1/10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  channel-group 12
#  mtu 9100
#  speed 100000
#  no shutdown
#
- name: Merges provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
     - name: PortChannel10
       members:
         interfaces:
           - member: Eth1/10
    state: merged
#
# After state:
# ------------
#
# interface Eth1/10
#  channel-group 10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  channel-group 12
#  mtu 9100
#  speed 100000
#  no shutdown
#
# Using replaced
#
# Before state:
# -------------
#
# interface Eth1/5
#   channel-group 10
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/6
#   channel-group 20
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/7
#   no channel-group
#   mtu 9100
#   speed 100000
#   no shutdown
#
- name: Replace device configuration of specified LAG attributes
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
      - name: PortChannel10
        members:
          interfaces:
            - member: Eth1/7
    state: replaced
#
# After state:
# ------------
#
# interface Eth1/5
#   no channel-group
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/6
#   channel-group 20
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/7
#   channel-group 10
#   mtu 9100
#   speed 100000
#   no shutdown
#
# Using overridden
#
# Before state:
# -------------
#
# interface Eth1/5
#   channel-group 10
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/6
#   no channel-group
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/7
#   channel-group 2
#   mtu 9100
#   speed 100000
#   no shutdown
#
- name: Override device configuration of all LAG attributes
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
      - name: PortChannel20
        members:
          interfaces:
            - member: Eth1/6
    state: overridden
#
# After state:
# ------------
# interface Eth1/5
#   no channel-group
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/6
#   channel-group 20
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/7
#   no channel-group
#   mtu 9100
#   speed 100000
#   no shutdown
#
# Using deleted
#
# Before state:
# -------------
# interface PortChannel10
# !
# interface Eth1/10
#  channel-group 10
#  mtu 9100
#  speed 100000
#  no shutdown
#
- name: Deletes LAG attributes of a given interface, This does not delete the port-channel itself
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
     - name: PortChannel10
       members:
         interfaces:
    state: deleted
#
# After state:
# ------------
# interface PortChannel10
# !
# interface Eth1/10
#  mtu 9100
#  speed 100000
#  no shutdown
#
# Using deleted
#
# Before state:
# -------------
# interface PortChannel 10
# !
# interface PortChannel 12
# !
# interface Eth1/10
#  channel-group 10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  channel-group 12
#  mtu 9100
#  speed 100000
#  no shutdown
#
- name: Deletes all LAGs and LAG attributes of all interfaces
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
    state: deleted
#
# After state:
# -------------
#
# interface Eth1/10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  mtu 9100
#  speed 100000
#  no shutdown
#
#
"""
RETURN = """
before:
  description: The configuration prior to the module invocation.
  returned: always
  type: list
  sample: >
    The configuration that is returned is always in the same format
    as the parameters above.
after:
  description: The resulting configuration module invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned is always in the same format
    as the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.lag_interfaces.lag_interfaces import Lag_interfacesArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.lag_interfaces.lag_interfaces import Lag_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Lag_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Lag_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
