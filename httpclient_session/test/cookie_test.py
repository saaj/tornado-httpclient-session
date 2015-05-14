from httpclient_session.test.testcase import AsyncHTTPTestCase



class CookieTestCase(AsyncHTTPTestCase):

    def test_persistence_of_cookie(self):
        self.http_client.fetch(self.get_url('/cookie'), self.stop)
        response = self.wait()
        self.assertIn('set-cookie', response.headers)

        self.http_client.fetch(self.get_url('/cookie'), self.stop)
        response = self.wait()
        self.assertIn('cookie', response.request.headers)
