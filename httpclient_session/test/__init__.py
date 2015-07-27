import tornado.testing
import tornado.web
from tornado.ioloop import IOLoop

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


class CookieHandler(tornado.web.RequestHandler):

    def get(self):
        if not self.get_cookie('key'):
            self.set_cookie('key', 'value')
        self.write('ok')


app = tornado.web.Application([
    (r'/cookie', CookieHandler),
], cookie_secret='N\xe8gH& M\xa5\xa3\x94&\xb9H\xb8\x96\x9e5\x89\xef3k'
    '\x85\xfd\xc7\xadmT\xd8(\x96\xdfX')

