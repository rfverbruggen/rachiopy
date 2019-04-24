import unittest
from rachiopy import Rachio

from tests.data import authtoken


class TestRachioMethods(unittest.TestCase):
    def test_validate_authtoken(self):
        rachio = Rachio(authtoken)

        self.assertEqual(rachio._headers, {'Content-Type': 'application/json',
                         'Authorization': 'Bearer %s' % authtoken})
