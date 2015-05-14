from httpclient_session.test.testcase import AsyncHTTPTestCase



class CookieTestCase(AsyncHTTPTestCase):

    def test_persistence_of_cookie(self):
        response = self.fetch('/cookie')
        self.assertIn('set-cookie', response.headers)

        response = self.fetch('/cookie')
        self.assertIn('cookie', response.request.headers)
