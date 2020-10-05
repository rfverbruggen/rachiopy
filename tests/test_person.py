"""Person object test module"""

import unittest
from unittest.mock import patch
import uuid

from rachiopy import Person
from tests.constants import BASE_API_URL, AUTHTOKEN, RESPONSE200


class TestPersonMethods(unittest.TestCase):
    """Class containing the Rachio object test cases."""

    def setUp(self):
        self.person = Person(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.person.authtoken, AUTHTOKEN)

    @patch("requests.Session.request")
    def test_info(self, mock):
        """Test if the info method works as expected."""

        mock.return_value = RESPONSE200

        self.person.info()

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{BASE_API_URL}/person/info")
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_get(self, mock):
        """Test if the get method works as expected."""
        mock.return_value = RESPONSE200

        personid = uuid.uuid4()

        self.person.get(personid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{BASE_API_URL}/person/{personid}")
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)
