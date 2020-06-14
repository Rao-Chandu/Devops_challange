import os
import sys
import time
import subprocess
import requests

from unittest import TestCase

from server import APP_HOST, APP_PORT


class ServerTestCase(TestCase):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    server_path = os.path.join(dir_path, 'server.py')

    host = APP_HOST
    port = APP_PORT
    url = f'http://{host}:{port}'

    @classmethod
    def setUpClass(cls) -> None:
        sys.stdout.write('\nStarting web-server...\n')
        cls.process = subprocess.Popen(cls.server_path, stderr=subprocess.PIPE, shell=True)
        time.sleep(1)
        sys.stdout.write(f'Server is listening on "{cls.url}"\n')

    def test_as_guest(self):
        res = requests.get(f'{self.url}/hello')
        data = res.json()

        self.assertIn('name', data.keys())
        self.assertIn('greeting', data.keys())
        self.assertIn('guest', data['name'])

    def test_as_user(self):
        res = requests.get(f'{self.url}/hello/World')
        data = res.json()

        self.assertIn('name', data.keys())
        self.assertIn('greeting', data.keys())
        self.assertIn('World', data['name'])

    @classmethod
    def tearDownClass(cls) -> None:
        sys.stdout.write('\nStopping web-server...\n')
        time.sleep(1)
