"""Rachio object test module"""

import unittest
from rachiopy import Rachio
from tests.constants import AUTHTOKEN


class TestRachioMethods(unittest.TestCase):
    """Class containing the Rachio object test cases."""

    def test_init(self):
        """Test if the constructor works as expected."""
        rachio = Rachio(AUTHTOKEN)

        self.assertEqual(rachio.authtoken, AUTHTOKEN)
        self.assertEqual(rachio.person.authtoken, AUTHTOKEN)
        self.assertEqual(rachio.device.authtoken, AUTHTOKEN)
        self.assertEqual(rachio.zone.authtoken, AUTHTOKEN)
        self.assertEqual(rachio.schedulerule.authtoken, AUTHTOKEN)
        self.assertEqual(rachio.flexschedulerule.authtoken, AUTHTOKEN)
        self.assertEqual(rachio.notification.authtoken, AUTHTOKEN)
        self.assertEqual(rachio.valve.authtoken, AUTHTOKEN)
        self.assertEqual(rachio.summary.authtoken, AUTHTOKEN)
        self.assertEqual(rachio.program.authtoken, AUTHTOKEN)
