# -*- coding: utf-8 -*-
#  Copyright 2021-2026 INFINI Labs
#
#  This file is part of Easysearch Python Client, which is derived from
#  Elasticsearch Python Client.
#  Copyright 2013-2020 Elasticsearch B.V.
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

# type: ignore

import time
import os
from unittest import TestCase, SkipTest

from easysearch import Easysearch
from easysearch.exceptions import ConnectionError


def get_test_client(nowait=False, **kwargs):
    # construct kwargs from the environment
    kw = {"timeout": 30, "ca_certs": ".ci/certs/ca.pem"}

    if "PYTHON_CONNECTION_CLASS" in os.environ:
        from easysearch import connection

        kw["connection_class"] = getattr(
            connection, os.environ["PYTHON_CONNECTION_CLASS"]
        )

    kw.update(kwargs)
    client = Easysearch([os.environ.get("EASYSEARCH_HOST", {})], **kw)

    # wait for yellow status
    for _ in range(1 if nowait else 100):
        try:
            client.cluster.health(wait_for_status="yellow")
            return client
        except ConnectionError:
            time.sleep(0.1)
    else:
        # timeout
        raise SkipTest("Easysearch failed to start.")


def _get_version(version_string):
    if "." not in version_string:
        return ()
    version = version_string.strip().split(".")
    return tuple(int(v) if v.isdigit() else 999 for v in version)


class EasysearchTestCase(TestCase):
    @staticmethod
    def _get_client():
        return get_test_client()

    @classmethod
    def setup_class(cls):
        cls.client = cls._get_client()

    def teardown_method(self, _):
        # Hidden indices expanded in wildcards in Easysearch 1.x+
        expand_wildcards = ["open", "closed"]
        if self.es_version() >= (1, 0):
            expand_wildcards.append("hidden")

        self.client.indices.delete(
            index="*", ignore=404, expand_wildcards=expand_wildcards
        )
        self.client.indices.delete_template(name="*", ignore=404)

    def es_version(self):
        if not hasattr(self, "_es_version"):
            version_string = self.client.info()["version"]["number"]
            self._es_version = _get_version(version_string)
        return self._es_version
