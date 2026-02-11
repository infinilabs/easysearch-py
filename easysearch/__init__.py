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

# flake8: noqa
from __future__ import absolute_import

import re
import sys
import logging
import warnings

from ._version import __versionstr__

_major, _minor, _patch = [
    int(x) for x in re.search(r"^(\d+)\.(\d+)\.(\d+)", __versionstr__).groups()
]
VERSION = __version__ = (_major, _minor, _patch)

logger = logging.getLogger("easysearch")
logger.addHandler(logging.NullHandler())

from .client import Easysearch
from .transport import Transport
from .connection_pool import ConnectionPool, ConnectionSelector, RoundRobinSelector
from .serializer import JSONSerializer
from .connection import Connection, RequestsHttpConnection, Urllib3HttpConnection
from .exceptions import (
    ImproperlyConfigured,
    EasysearchException,
    SerializationError,
    TransportError,
    NotFoundError,
    ConflictError,
    RequestError,
    ConnectionError,
    SSLError,
    ConnectionTimeout,
    AuthenticationException,
    AuthorizationException,
    EasysearchDeprecationWarning,
)

# Only raise one warning per deprecation message so as not
# to spam up the user if the same action is done multiple times.
warnings.simplefilter("default", category=EasysearchDeprecationWarning, append=True)

__all__ = [
    "Easysearch",
    "Transport",
    "ConnectionPool",
    "ConnectionSelector",
    "RoundRobinSelector",
    "JSONSerializer",
    "Connection",
    "RequestsHttpConnection",
    "Urllib3HttpConnection",
    "ImproperlyConfigured",
    "EasysearchException",
    "SerializationError",
    "TransportError",
    "NotFoundError",
    "ConflictError",
    "RequestError",
    "ConnectionError",
    "SSLError",
    "ConnectionTimeout",
    "AuthenticationException",
    "AuthorizationException",
    "EasysearchDeprecationWarning",
]

try:
    # Asyncio only supported on Python 3.6+
    if sys.version_info < (3, 6):
        raise ImportError

    from ._async.http_aiohttp import AIOHttpConnection, AsyncConnection
    from ._async.transport import AsyncTransport
    from ._async.client import AsyncEasysearch

    __all__ += [
        "AIOHttpConnection",
        "AsyncConnection",
        "AsyncTransport",
        "AsyncEasysearch",
    ]
except (ImportError, SyntaxError):
    pass
