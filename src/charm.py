#!/usr/bin/env python3
# Copyright 2021 Dylan Stephano-Shachter
# See LICENSE file for licensing details.

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

    https://discourse.charmhub.io/t/4208
"""

import logging

import charms.cassandra.v1.cql as charmlib

from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)

IMAGE_DETAILS = {"imagePath": "dstathis/cassandra-stress"}


class CassandraStressOperatorCharm(CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.simpletest_action, self.on_simple_test)
        self.framework.observe(self.on.stresstest_action, self.on_stress_test)
        self.framework.observe(self.on.install, self.setup)
        self.consumer = charmlib.CQLConsumer(self, "cql", {"consumes": {}})

    def setup(self, event):
        self.model.pod.set_spec(self.get_pod_spec(["sleep", "infinity"]))
        self.unit.status = ActiveStatus()

    def get_pod_spec(self, command):
        spec = {
            "version": 3,
            "containers": [
                {
                    "name": self.app.name,
                    "imageDetails": IMAGE_DETAILS,
                    "command": command,
                    "ports": [
                        {
                            "containerPort": 22,
                            "name": "ssh",
                            "protocol": "TCP",
                        }
                    ],
                }
            ],
        }
        return spec

    def on_simple_test(self, event):
        self.consumer.request_databases(1)
        logger.error(self.consumer.credentials())
        logger.error(self.consumer.databases())
        logger.error(self.consumer.port())

    def on_stress_test(self, event):
        pass


if __name__ == "__main__":
    main(CassandraStressOperatorCharm)
