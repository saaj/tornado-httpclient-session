import tornado.testing

from tornado.test.util import unittest

TEST_MODULES = [
    'httpclient_session.test.cookie_test',
]


def all():
    return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)


def main():
    tornado.testing.main()

if __name__ == '__main__':
    main()
