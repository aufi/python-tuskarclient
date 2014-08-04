# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import mock

import tuskarclient.tests.utils as tutils
from tuskarclient.v2 import plans


class PlanManagerTest(tutils.TestCase):

    def setUp(self):
        """Create a mock API object and bind to the PlanManager manager.
        """
        super(PlanManagerTest, self).setUp()
        self.api = mock.Mock()
        self.pm = plans.PlanManager(self.api)