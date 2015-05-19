from httpclient_session.mocks import MockRequest, MockResponse


def extract_cookies_to_jar(jar, request, response):
    req = MockRequest(request)
    res = MockResponse(response)

    jar.extract_cookies(res, req)
