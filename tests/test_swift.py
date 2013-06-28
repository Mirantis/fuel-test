#!/usr/bin/env python

import unittest
from helpers.vm_test_case import CobblerTestCase
from helpers.manifest import Manifest
from settings import PUPPET_AGENT_COMMAND


class SwiftCase(CobblerTestCase):
    def test_swift(self):
        Manifest.write_manifest(
            self.remote(),
            Manifest().generate_swift_manifest(
                controllers=self.nodes().controllers)
        )
        self.validate(self.nodes().controllers[0], PUPPET_AGENT_COMMAND)
        self.do(self.nodes().storages, PUPPET_AGENT_COMMAND)
        self.do(self.nodes().storages, PUPPET_AGENT_COMMAND)
        self.validate(self.nodes().proxies[0], PUPPET_AGENT_COMMAND)
        self.validate(self.nodes().storages, PUPPET_AGENT_COMMAND)

if __name__ == '__main__':
    unittest.main()
