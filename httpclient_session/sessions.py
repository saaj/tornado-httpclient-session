from tornado.httpclient import HTTPRequest, AsyncHTTPClient

from httpclient_session.mocks import MockRequest
from httpclient_session.cookies import extract_cookies_to_jar
from httpclient_session.contrib.cookies import RequestsCookieJar


class Session(object):

    def __init__(self, httpclient_class=None, **kwargs):
        if httpclient_class is None:
            httpclient_class = AsyncHTTPClient

        self._httpclient = httpclient_class(**kwargs)
        self._closed = False

        self.cookies = RequestsCookieJar()

    def __del__(self):
        self.close()

    def __getattr__(self, name):
        return getattr(self._httpclient, name)

    def close(self):
        if not self._closed:
            if not self._httpclient._closed:
                self._httpclient.close()
            self._closed = True

    def fetch(self, request, callback=None, raise_error=True, **kwargs):
        if self._closed:
            raise RuntimeError("fetch() called on closed session")
        if not isinstance(request, HTTPRequest):
            request = HTTPRequest(url=request)

        request = self.prepare_request(request)
        callback = self.prepare_callback(callback)

        result = self._httpclient.fetch(request,
                                        callback=callback,
                                        raise_error=raise_error,
                                        **kwargs)

        return result

    def prepare_request(self, request):
        req = MockRequest(request)
        self.cookies.add_cookie_header(req)

        return request

    def prepare_callback(self, callback=None):

        def wrapper(response):
            extract_cookies_to_jar(self.cookies, response.request, response)

            if callback:
                return callback(response)

        return wrapper
