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

from __future__ import unicode_literals

from . import EasysearchTestCase


class TestUnicode(EasysearchTestCase):
    def test_indices_analyze(self):
        self.client.indices.analyze(body='{"text": "привет"}')


class TestBulk(EasysearchTestCase):
    def test_bulk_works_with_string_body(self):
        docs = '{ "index" : { "_index" : "bulk_test_index", "_id" : "1" } }\n{"answer": 42}'
        response = self.client.bulk(body=docs)

        self.assertFalse(response["errors"])
        self.assertEqual(1, len(response["items"]))

    def test_bulk_works_with_bytestring_body(self):
        docs = b'{ "index" : { "_index" : "bulk_test_index", "_id" : "2" } }\n{"answer": 42}'
        response = self.client.bulk(body=docs)

        self.assertFalse(response["errors"])
        self.assertEqual(1, len(response["items"]))
