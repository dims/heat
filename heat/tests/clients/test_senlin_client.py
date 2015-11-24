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

from testtools import testcase

from heat.tests import common
from heat.tests import utils


class SenlinClientPluginTests(common.HeatTestCase):

    @testcase.skip('skipped until bug #1519185 is fixed!')
    def test_cluster_get(self):
        context = utils.dummy_context()
        plugin = context.clients.client_plugin('senlin')
        client = plugin.client()
        self.assertIsNotNone(client.clusters)
