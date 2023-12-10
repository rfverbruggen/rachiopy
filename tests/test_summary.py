"""Summary object test module"""

import unittest
import uuid
import json
from unittest.mock import patch

from rachiopy import SummaryServce
from tests.constants import VALVE_API_URL, AUTHTOKEN, RESPONSE200


class TestSummaryMethod(unittest.TestCase):
    """Class containing the Summary object test."""

    def setUp(self):
        self.summary = SummaryServce(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.summary.authtoken, AUTHTOKEN)

    @patch("requests.Session.request")
    def test_get_valve_day_views(self, mock):
        """Test if the get day views method works as expected."""
        mock.return_value = RESPONSE200

        deviceid = str(uuid.uuid4())
        start = {"year": 2023, "month": 1, "day": 1}
        end = {"year": 2023, "month": 1, "day": 30}

        self.summary.get_valve_day_views(deviceid, start, end)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{VALVE_API_URL}/summary/getValveDayViews")
        self.assertEqual(args[0], "POST")
        self.assertEqual(
            kwargs["data"],
            json.dumps(
                {
                    "resourceId": {"baseStationId": deviceid},
                    "start": start,
                    "end": end
                }
                )
            )
