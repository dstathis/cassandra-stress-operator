# Copyright 2021 Dylan Stephano-Shachter
# See LICENSE file for licensing details.

import unittest

from ops.testing import Harness
from charm import CassandraStressOperatorCharm


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness(CassandraStressOperatorCharm)
        self.addCleanup(self.harness.cleanup)
        self.harness.set_leader(True)
        self.harness.begin_with_initial_hooks()

    def test_pass(self):
        pass
