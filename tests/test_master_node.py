#    Copyright 2013 Mirantis, Inc.
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


import logging
import unittest
import xmlrpclib
from devops.helpers.helpers import wait, tcp_ping, http
from helpers.decorators import debug, fetch_logs
from tests.fuel_testcase import FuelTestCase


logger = logging.getLogger(__name__)
logwrap = debug(logger)


class TestMasterNode(FuelTestCase):
    @logwrap
    def test_puppetmaster_alive(self):
        wait(
            lambda: tcp_ping(self.get_master_ip(), 8140), timeout=5
        )
        ps_output = self.get_master_ssh().execute('ps ax')['stdout']
        pm_processes = filter(lambda x: '/usr/sbin/puppetmasterd' in x, ps_output)
        logging.debug("Found puppet master processes: %s" % pm_processes)
        self.assertEquals(len(pm_processes), 4)

    @logwrap
    def test_cobbler_alive(self):
        wait(
            lambda: http(host=self.get_master_ip(), url='/cobbler_api',
                         waited_code=502),
            timeout=60
        )
        server = xmlrpclib.Server(
            'http://%s/cobbler_api' % self.get_master_ip())
        # raises an error if something isn't right
        server.login('cobbler', 'cobbler')

    @logwrap
    @fetch_logs
    def test_nailyd_alive(self):
        ps_output = self.get_master_ip().execute('ps ax')['stdout']
        naily_master = filter(lambda x: 'naily master' in x, ps_output)
        logging.debug("Found naily processes: %s" % naily_master)
        self.assertEquals(len(naily_master), 1)
        naily_workers = filter(lambda x: 'naily worker' in x, ps_output)
        logging.debug(
            "Found %d naily worker processes: %s" %
            (len(naily_workers), naily_workers))
        self.assertEqual(True, len(naily_workers) > 1)

    @logwrap
    @fetch_logs
    def test_config_astute(self):
        self.generate_astute_config()


if __name__ == '__main__':
    unittest.main()
