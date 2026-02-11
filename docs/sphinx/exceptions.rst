.. _exceptions:

Exceptions
==========

.. py:module:: easysearch

.. autoclass:: ImproperlyConfigured

.. autoclass:: EasysearchException

.. autoclass:: SerializationError(EasysearchException)

.. autoclass:: TransportError(EasysearchException)
   :members:

.. autoclass:: ConnectionError(TransportError)
.. autoclass:: ConnectionTimeout(ConnectionError)
.. autoclass:: SSLError(ConnectionError)

.. autoclass:: NotFoundError(TransportError)
.. autoclass:: ConflictError(TransportError)
.. autoclass:: RequestError(TransportError)
.. autoclass:: AuthenticationException(TransportError)
.. autoclass:: AuthorizationException(TransportError)
