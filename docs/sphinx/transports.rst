.. _transports:

Transport classes
=================

List of transport classes that can be used, simply import your choice and pass
it to the constructor of :class:`~easysearch.Easysearch` as
`connection_class`. Note that the
:class:`~easysearch.connection.RequestsHttpConnection` requires ``requests``
to be installed.

For example to use the ``requests``-based connection just import it and use it:

.. code-block:: python

    from easysearch import Easysearch, RequestsHttpConnection
    es = Easysearch(connection_class=RequestsHttpConnection)

The default connection class is based on ``urllib3`` which is more performant
and lightweight than the optional ``requests``-based class. Only use
``RequestsHttpConnection`` if you have need of any of ``requests`` advanced
features like custom auth plugins etc.


.. py:module:: easysearch.connection

Connection
----------

.. autoclass:: Connection

Urllib3HttpConnection
---------------------

.. autoclass:: Urllib3HttpConnection


RequestsHttpConnection
----------------------

.. autoclass:: RequestsHttpConnection

