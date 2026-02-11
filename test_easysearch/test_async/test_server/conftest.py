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

import os
import pytest
import asyncio
import easysearch
from ...utils import wipe_cluster

pytestmark = pytest.mark.asyncio


@pytest.fixture(scope="function")
async def async_client():
    client = None
    try:
        if not hasattr(easysearch, "AsyncEasysearch"):
            pytest.skip("test requires 'AsyncEasysearch'")

        kw = {
            "timeout": 3,
            "ca_certs": ".ci/certs/ca.pem",
            "connection_class": easysearch.AIOHttpConnection,
        }

        client = easysearch.AsyncEasysearch(
            [os.environ.get("EASYSEARCH_HOST", {})], **kw
        )

        # wait for yellow status
        for _ in range(100):
            try:
                await client.cluster.health(wait_for_status="yellow")
                break
            except ConnectionError:
                await asyncio.sleep(0.1)
        else:
            # timeout
            pytest.skip("Easysearch failed to start.")

        yield client

    finally:
        if client:
            wipe_cluster(client)
            await client.close()
