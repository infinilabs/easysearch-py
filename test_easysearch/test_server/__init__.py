#  Copyright 2021-2026 INFINI Labs
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

from unittest import SkipTest
from easysearch.helpers import test
from easysearch.helpers.test import EasysearchTestCase as BaseTestCase

client = None


def get_client(**kwargs):
    global client
    if client is False:
        raise SkipTest("No client is available")
    if client is not None and not kwargs:
        return client

    # try and locate manual override in the local environment
    try:
        from test_easysearch.local import get_client as local_get_client

        new_client = local_get_client(**kwargs)
    except ImportError:
        # fallback to using vanilla client
        try:
            new_client = test.get_test_client(**kwargs)
        except SkipTest:
            client = False
            raise

    if not kwargs:
        client = new_client

    return new_client


def setup_module():
    get_client()


class EasysearchTestCase(BaseTestCase):
    @staticmethod
    def _get_client(**kwargs):
        return get_client(**kwargs)
