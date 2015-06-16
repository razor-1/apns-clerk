apns-clerk.
===========

Python client for `Apple Push Notification service (APNs) <https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html>`_.

This project is forked from apns-client, as there was a tiny but severe problem with SSL handshake rendering the package to be unusable.
For the time being please check for apns-client's `documentation <http://apns-client.readthedocs.org>`_ .


Requirements
------------

- `six <https://pypi.python.org/pypi/six/>`_ - Python 2 and 3 compatibility library.
- `pyOpenSSL <https://pypi.python.org/pypi/pyOpenSSL/>`_ - OpenSSL wrapper. Required by standard networking back-end.

Standard library has support for `SSL transport
<http://docs.python.org/2/library/ssl.html>`_. However, it is impossible to use
it with certificates provided as a string. We store certificates in database,
because we handle different apps on many Celery worker machines. A dirty
solution would be to create temporary files, but it is insecure and slow. So,
we have decided to use a better OpenSSL wrapper and ``pyOpenSSL`` was the
easiest to handle. ``pyOpenSSL`` is loaded on demand by standard networking
back-end. If you use your own back-end, based on some other SSL implementation,
then you don't have to install ``pyOpenSSL``.


Changelog
---------
*v0.2.0*
    Added support for sending multiple pushes with varying payload during one APNs connection, thanks Jon Snyder!
*v0.1.2*
    Removed not needed non ascii character which was causing problems with python < 3
*v0.1.1*
    Imported changes from open apns-client pull requests. Thanks Jason Spafford, zhe li and neetu jain.
*v0.1*
    Forked from apns-client and fixed SSL handshake error caused by Apple's SSLv3 deprecation


Alternatives
------------

There are `many alternatives <https://pypi.python.org/pypi?%3Aaction=search&term=apns&submit=search>`_ available.
This library differs in the following design decisions:

- *Support certificates from strings*. We do not distribute certificate files
  on worker machines, they fetch it from the database when needed. This
  approach simplifies deployment, upgrades and maintenance.
- *Keep connections persistent*. An SSL handshaking round is slow. Once
  connection is established, it should remain open for at least few minutes,
  waiting for the next batch.
- *Support enhanced format*. Apple developers have designed a notoriously bad
  push protocol. They have upgraded it to enhanced version, which makes it
  possible to detect which messages in the batch have failed.
- *Clean pythonic API*. No need for lots of classes, long lists of exceptions etc.
- *Do not hard-code validation, let APNs fail*. This decision makes library
  a little bit more future proof.


Todo
----

- *[TODO] own documentation for apns-clerk*
- *[TODO] proper attributions for previous work*
