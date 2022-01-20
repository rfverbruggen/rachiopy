"""ScheduleRule object test module"""

import unittest
from unittest.mock import patch
import uuid
import json

from rachiopy import Schedulerule
from tests.constants import BASE_API_URL, AUTHTOKEN, RESPONSE200, RESPONSE204


class TestScheduleRuleMethods(unittest.TestCase):
    """Class containing the ScheduleRule object test cases."""

    def setUp(self):
        self.schedulerule = Schedulerule(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.schedulerule.authtoken, AUTHTOKEN)

    @patch("requests.Session.request")
    def test_get(self, mock):
        """Test if the get method works as expected."""
        mock.return_value = RESPONSE200

        scheduleruleid = str(uuid.uuid4())

        self.schedulerule.get(scheduleruleid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{BASE_API_URL}/schedulerule/{scheduleruleid}"
        )
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_skip(self, mock):
        """Test if the skip method works as expected."""
        mock.return_value = RESPONSE204

        scheduleruleid = str(uuid.uuid4())

        self.schedulerule.skip(scheduleruleid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{BASE_API_URL}/schedulerule/skip")
        self.assertEqual(args[0], "PUT")
        self.assertEqual(kwargs["data"], json.dumps({"id": scheduleruleid}))

    @patch("requests.Session.request")
    def test_start(self, mock):
        """Test if the start method works as expected."""
        mock.return_value = RESPONSE204

        scheduleruleid = str(uuid.uuid4())

        self.schedulerule.start(scheduleruleid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{BASE_API_URL}/schedulerule/start")
        self.assertEqual(args[0], "PUT")
        self.assertEqual(kwargs["data"], json.dumps({"id": scheduleruleid}))

    @patch("requests.Session.request")
    def test_seasonal_adjustment(self, mock):
        """Test if the seasonal adjustment method works as expected."""
        mock.return_value = RESPONSE200

        scheduleruleid = str(uuid.uuid4())
        adjustment = 0.2

        self.schedulerule.seasonal_adjustment(scheduleruleid, adjustment)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{BASE_API_URL}/schedulerule/seasonal_adjustment"
        )
        self.assertEqual(args[0], "PUT")
        self.assertEqual(
            kwargs["data"],
            json.dumps({"id": scheduleruleid, "adjustment": adjustment}),
        )
