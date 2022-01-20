"""FlexScheduleRule object test module"""

import unittest
from unittest.mock import patch
import uuid

from rachiopy import FlexSchedulerule
from tests.constants import BASE_API_URL, AUTHTOKEN, RESPONSE200


class TestFlexScheduleRuleMethods(unittest.TestCase):
    """Class containing the FlexScheduleRule object test cases."""

    def setUp(self):
        self.flexschedulerule = FlexSchedulerule(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.flexschedulerule.authtoken, AUTHTOKEN)

    @patch("requests.Session.request")
    def test_get(self, mock):
        """Test if the get method works as expected."""
        mock.return_value = RESPONSE200

        flexscheduleruleid = uuid.uuid4()

        self.flexschedulerule.get(flexscheduleruleid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1],
            f"{BASE_API_URL}/flexschedulerule/{flexscheduleruleid}",
        )
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)
