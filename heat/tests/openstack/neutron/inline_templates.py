#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

SPOOL_TEMPLATE = '''
heat_template_version: 2015-04-30
description: Template to test subnetpool Neutron resource
resources:
  sub_pool:
    type: OS::Neutron::SubnetPool
    properties:
      name: the_sp
      prefixes:
        - 10.1.0.0/16
      address_scope: test
      default_quota: 2
      default_prefixlen: 28
      min_prefixlen: 8
      max_prefixlen: 32
      is_default: False
      tenant_id: c1210485b2424d48804aad5d39c61b8f
      shared: False
'''

SPOOL_MINIMAL_TEMPLATE = '''
heat_template_version: 2015-04-30
description: Template to test subnetpool Neutron resource
resources:
  sub_pool:
    type: OS::Neutron::SubnetPool
    properties:
      prefixes:
        - 10.0.0.0/16
        - 10.1.0.0/16
'''
