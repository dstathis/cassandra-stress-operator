#!/usr/bin/env python3

#  Copyright 2021 Canonical Ltd.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

    https://discourse.charmhub.io/t/4208
"""

import logging

import charms.cassandra_k8s.v0.cql as charmlib

from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)

IMAGE_DETAILS = {"imagePath": "dstathis/cassandra-stress"}


class CassandraStressOperatorCharm(CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)
        self._container = self.unit.get_container("cassandra-stress")
        self.framework.observe(self.on.simpletest_action, self.on_simple_test)
        self.framework.observe(self.on["cql"].relation_changed, self.print_db_info)
        self.framework.observe(self.on.stresstest_action, self.on_stress_test)
        self.framework.observe(self.on.cassandra_stress_pebble_ready, self.setup)
        self.consumer = charmlib.CassandraConsumer(self, "cql")

    def setup(self, event):
        layer = {
            "summary": "Cassandra Stress Layer",
            "description": "pebble config layer for Cassandra Stress",
        }
        self._container.add_layer("cassandra-stress", layer, combine=True)
        self.unit.status = ActiveStatus()

    def on_simple_test(self, event):
        pass

    def print_db_info(self, _):
        logger.error(self.consumer.credentials())
        logger.error(self.consumer.port())

    def on_stress_test(self, event):
        pass


if __name__ == "__main__":
    main(CassandraStressOperatorCharm)
