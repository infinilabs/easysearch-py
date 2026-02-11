.. _changelog:

Changelog
=========

0.1.0 (2026-02-11)
------------------

**Initial Beta Release of Easysearch Python Client**

This is the first beta release of the official Python client for Easysearch, forked from
the Elasticsearch Python client 7.10.2 under the Apache 2.0 license.

**Note**: This is a beta version (0.1.0) for testing and gathering community feedback.
A stable 1.0.0 release will follow after further testing and validation.

**New Features:**

* Complete brand refactoring from Elasticsearch to Easysearch
* Full API compatibility with Easysearch 1.x and 2.x
* Removed X-Pack commercial features (not applicable to Apache 2.0 fork)
* Support for both synchronous and asynchronous operations via ``Easysearch`` and ``AsyncEasysearch``
* Type stubs (.pyi files) for static type checking and IDE auto-complete
* Comprehensive helper utilities: ``bulk``, ``streaming_bulk``, ``scan``, ``reindex``
* HTTP compression support for bandwidth-constrained networks
* Connection pooling and automatic node discovery
* Maintained backward compatibility: ``Elasticsearch`` class name available as alias
* All license headers standardized to Apache 2.0
* Documentation updated for Easysearch branding

**Core APIs Supported:**

* Index operations: index, get, update, delete, bulk
* Search operations: search, msearch, scroll, clear_scroll
* Cluster operations: health, state, stats, settings
* Indices operations: create, delete, refresh, flush, settings, mappings
* Nodes operations: info, stats, usage
* Snapshot operations: create, restore, delete, status
* Ingest operations: put_pipeline, get_pipeline, delete_pipeline
* Task management: list, get, cancel
* Cat APIs: complete set of cluster information APIs

**Python Support:**

* Python 2.7, 3.4+
* Type hints for Python 3.5+
* Async/await support for Python 3.6+

**Installation:**

.. code-block:: bash

    pip install easysearch

**Basic Usage:**

.. code-block:: python

    from easysearch import Easysearch
    
    # Create client
    es = Easysearch(['localhost:9200'])
    
    # Index a document
    es.index(index='test', id=1, body={'field': 'value'})
    
    # Search
    result = es.search(index='test', body={'query': {'match_all': {}}})

---

**Historical Note:**

The version history below represents the upstream Elasticsearch Python client
development history. Easysearch Python client 1.0.0 is based on Elasticsearch
Python client 7.10.2 and starts a new version sequence.

The historical changelog is preserved below for reference purposes only.

---

Upstream Elasticsearch History
===============================

7.10.2 (2020-12-16)
-------------------

* Base version for Easysearch fork
* Fixed scan helper scroll response handling
* IPv6 host handling improvements
* Python 3.9 compatibility (collections.abc.Mapping)

7.10.0 (2020-11-11)
-------------------

* Added support for Elasticsearch 7.10 APIs
* Added basic type stubs for static type checking
* Added Optimistic Concurrency Control to bulk helpers
* Fixed connection logging issues
* AsyncTransport timeout parameter fixes

7.9.0 (2020-08-18)
------------------

* Added support for Elasticsearch 7.9 APIs
* Fixed retry behavior with sniff_on_connection_error
* Improved error handling during sniffing

7.8.0 (2020-06-18)
------------------

* Added support for Elasticsearch 7.8 APIs
* Added async/await support via AsyncElasticsearch
* Added async helpers: async_bulk, async_streaming_bulk, async_scan
* Deprecated API route updates

7.7.0 (2020-05-13)
------------------

* Added support for Elasticsearch 7.7 APIs
* Added ElasticsearchDeprecationWarning for HTTP Warning headers
* Added numpy and pandas serialization support
* Added certifi as dependency for HTTPS

7.6.0 (2020-03-19)
------------------

* Added support for Elasticsearch 7.6 APIs
* Added X-Opaque-Id support for task identification
* Added HTTP compression to RequestsHttpConnection
* Updated cloud_id defaults

7.5.0 (2020-01-15)
------------------

* All APIs now auto-generated
* Deprecated .xpack namespace
* Support for Elasticsearch 7.5 APIs

7.0.0 (2019-04-11)
------------------

* Elasticsearch 7.0 compatibility
* Removed deprecated update_all_types option
* SSL verification warnings
* Support for both OSS and X-Pack flavors

6.0.0 - 6.8.1
-------------

* Elasticsearch 6.x compatibility releases
* HTTP compression support
* Cloud ID support
* X-Pack client integration

5.0.0 - 5.5.0
-------------

* Elasticsearch 5.x compatibility releases
* SSL certificate validation by default
* Custom HTTP headers support
* streaming_bulk with retry support

Earlier Versions (1.0.0 - 2.4.0)
--------------------------------

* Initial releases and Elasticsearch 1.x/2.x compatibility
* Basic client functionality
* Helper utilities development
* Connection pooling and transport layer

---

For the complete upstream history, see: https://github.com/infinilabs/elasticsearch-py
