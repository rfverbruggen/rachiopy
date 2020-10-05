"""ScheduleRule object test module"""

import unittest
from unittest.mock import patch
import uuid

from rachiopy import Schedulerule
from tests.constants import (
    BASE_API_URL,
    AUTHTOKEN,
    SUCCESS200HEADERS,
    SUCCESS204HEADERS,
    JSONBODY,
)


class TestScheduleRuleMethods(unittest.TestCase):
    """Class containing the ScheduleRule object test cases."""

    def setUp(self):
        self.schedulerule = Schedulerule(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.schedulerule.authtoken, AUTHTOKEN)

    @patch("httplib2.Http.request")
    def test_get(self, mock):
        """Test if the get method works as expected."""
        mock.return_value = (SUCCESS200HEADERS, JSONBODY)

        scheduleruleid = uuid.uuid4()

        self.schedulerule.get(scheduleruleid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[0], f"{BASE_API_URL}/schedulerule/" f"{scheduleruleid}"
        )
        self.assertEqual(args[1], "GET")
        self.assertEqual(kwargs["body"], None)

    @patch("httplib2.Http.request")
    def test_skip(self, mock):
        """Test if the skip method works as expected."""
        mock.return_value = (SUCCESS204HEADERS, None)

        scheduleruleid = uuid.uuid4()

        self.schedulerule.skip(scheduleruleid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/schedulerule/skip")
        self.assertEqual(args[1], "PUT")
        self.assertEqual(kwargs["body"], {"id": scheduleruleid})

    @patch("httplib2.Http.request")
    def test_start(self, mock):
        """Test if the start method works as expected."""
        mock.return_value = (SUCCESS204HEADERS, None)

        scheduleruleid = uuid.uuid4()

        self.schedulerule.start(scheduleruleid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/schedulerule/start")
        self.assertEqual(args[1], "PUT")
        self.assertEqual(kwargs["body"], {"id": scheduleruleid})

    @patch("httplib2.Http.request")
    def test_seasonal_adjustment(self, mock):
        """Test if the seasonal adjustment method works as expected."""
        mock.return_value = (SUCCESS200HEADERS, JSONBODY)

        scheduleruleid = uuid.uuid4()
        adjustment = 0.2

        self.schedulerule.seasonal_adjustment(scheduleruleid, adjustment)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[0], f"{BASE_API_URL}/schedulerule/seasonal_adjustment"
        )
        self.assertEqual(args[1], "PUT")
        self.assertEqual(
            kwargs["body"], {"id": scheduleruleid, "adjustment": adjustment}
        )
