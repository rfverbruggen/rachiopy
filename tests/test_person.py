"""Person object test module"""

import unittest
from unittest.mock import patch
import uuid

from rachiopy import Person
from tests.constants import (
    BASE_API_URL,
    AUTHTOKEN,
    SUCCESS200HEADERS,
    JSONBODY,
)


class TestPersonMethods(unittest.TestCase):
    """Class containing the Rachio object test cases."""

    def setUp(self):
        self.person = Person(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.person.authtoken, AUTHTOKEN)

    @patch("httplib2.Http.request")
    def test_info(self, mock_info):
        """Test if the info method works as expected."""

        mock_info.return_value = (SUCCESS200HEADERS, JSONBODY)

        self.person.info()

        args, kwargs = mock_info.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/person/info")
        self.assertEqual(args[1], "GET")
        self.assertEqual(kwargs["body"], None)

    @patch("httplib2.Http.request")
    def test_get(self, mock):
        """Test if the get method works as expected."""
        mock.return_value = (SUCCESS200HEADERS, JSONBODY)

        personid = uuid.uuid4()

        self.person.get(personid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/person/{personid}")
        self.assertEqual(args[1], "GET")
        self.assertEqual(kwargs["body"], None)
