try:
    from urlparse import urlparse, urlunparse
except ImportError:
    from urllib.parse import urlparse, urlunparse

from tornado.httputil import _normalized_headers


class MockRequest(object):

    def __init__(self, request):
        self._request = request

    def get_full_url(self):
        if not self._request.headers.get('host'):
            return self._request.url

        host = self._request.headers['host']
        parsed = urlparse(self._request.url)

        return urlunparse([
            parsed.scheme, host, parsed.path, parsed.params, parsed.query,
            parsed.fragment
        ])

    def get_host(self):
        return urlparse(self._request.url).netloc

    def get_type(self):
        return urlparse(self._request.url).scheme

    def is_unverifiable(self):
        return True

    @property
    def unverifiable(self):
        return self.is_unverifiable()

    def get_origin_req_host(self):
        return self.get_host()
    
    @property
    def origin_req_host(self):
        '''Python 3 compatibility'''
        
        return self.get_origin_req_host()

    def has_header(self, name):
        return name in self._request.headers

    def get_header(self, name, default=None):
        return self._request.headers.get(name, default)

    def header_items(self):
        return self._request.headers.items()

    def add_unredirected_header(self, name, value):
        self._request.headers[name] = value


class MockResponse(object):

    def __init__(self, response):
        self._response = response

    def info(self):
        return self

    def getallmatchingheaders(self, name):
        norm_name = _normalized_headers[name]

        return ['{0}: {1}'.format(norm_name, value)
                for value in self._response.headers.get_list(name)]

    def getheaders(self, name):
        return self._response.headers.get_list(name)
    
    def get_all(self, name, failobj=None):
        '''Python 3 changes, see http://bugs.python.org/issue4773'''
        try:
            return self.getheaders(name)
        except KeyError:
            if failobj:
                return failobj
            else:
                raise

