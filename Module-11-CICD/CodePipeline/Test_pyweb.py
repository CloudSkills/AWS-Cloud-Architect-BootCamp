import os
import unittest

from application.application import application


application.testing = True


class FlaskTest(unittest.TestCase):
    def test_main(self):
        with application.test_client() as client:
            client.get('/')


if __name__ == '__main__':
    unittest.main()