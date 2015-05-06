Tornado-HttpClient-Session
==========================

A mimic inspired by the session feature in `Requests <https://github.com/kennethreitz/requests>`_, it adds support to `Tornado <https://github.com/tornadoweb/tornado>`_ that allows you to persist context such as cookies and other parameters across requests' fetching from `tornado.httpclient <http://tornado.readthedocs.org/en/latest/httpclient.html>`_.

**THIS IS SESSION ABOUT CLIENT, NOT SERVER!**

Installation
------------

    pip install tornado-httpclient-session

Usage
-----

.. code-block:: python

   from tornado.httpclient import HTTPClient

   from httpclient_session import Session

   s = Session(HTTPClient) # AsyncHTTPClient default

   r = s.fetch('https://github.com')
   print r.headers['set-cookie'] # Inspect cookies returnd from Github

   r = s.fetch('https://github.com') # Fetching carrys cookies
   print r.request.headers['cookie'] # Inspect cookies attached

Development Progress
--------------------

Persistences of:

* Cookies ✔
* Authorization ✘

Any Suggestions Welcome!
------------------------
