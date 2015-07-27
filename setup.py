#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.2.0'

setup(name='tornado-httpclient-session',
      version=VERSION,
      packages=['httpclient_session', 'httpclient_session.test',
                'httpclient_session.contrib'],
      author='mailto1587',
      author_email='mailto1587@gmail.com',
      description='Session support to tornado.httpclient.',
      license='http://opensource.org/licenses/MIT',
      url='https://github.com/mailto1587/tornado-httpclient-session',
      keywords=['Tornado', 'HttpClient', 'Session'],
      classifiers=[
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],      
      install_requires=[
          'tornado'
      ])
