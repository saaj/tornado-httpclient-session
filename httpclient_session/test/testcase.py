import tornado.testing

from tornado.ioloop import IOLoop

from httpclient_session.test.application import app
from httpclient_session import Session

session = Session(io_loop=IOLoop.current())


class AsyncHTTPTestCase(tornado.testing.AsyncHTTPTestCase):

    def __init__(self, methodName='runTest', **kwargs):
        super(AsyncHTTPTestCase, self).__init__(methodName, **kwargs)

    def get_app(self):
        return app

    def get_new_ioloop(self):
        return IOLoop.current()

    def get_http_client(self):
        return session
