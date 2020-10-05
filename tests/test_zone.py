"""Zone object test module"""

import unittest
from unittest.mock import patch
import uuid
import random

from random import randrange
from rachiopy import Zone
from rachiopy.zone import ZoneSchedule
from tests.constants import (
    BASE_API_URL,
    AUTHTOKEN,
    SUCCESS200HEADERS,
    SUCCESS204HEADERS,
    JSONBODY,
)


class TestZoneMethods(unittest.TestCase):
    """Class containing the Zone object test cases."""

    def setUp(self):
        self.zone = Zone(AUTHTOKEN)

        zone1id = uuid.uuid4()
        zone2id = uuid.uuid4()
        zone3id = uuid.uuid4()
        duration1 = randrange(10800)
        duration2 = randrange(10800)
        duration3 = randrange(10800)

        self.zones = []
        self.zones.append((zone1id, duration1))
        self.zones.append((zone2id, duration2))
        self.zones.append((zone3id, duration3))

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.zone.authtoken, AUTHTOKEN)

    @patch("httplib2.Http.request")
    def test_get(self, mock):
        """Test if the get method works as expected."""
        mock.return_value = (SUCCESS200HEADERS, JSONBODY)

        zoneid = uuid.uuid4()

        self.zone.get(zoneid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/zone/" f"{zoneid}")
        self.assertEqual(args[1], "GET")
        self.assertEqual(kwargs["body"], None)

    @patch("httplib2.Http.request")
    def test_start(self, mock):
        """Test if the start method works as expected."""
        mock.return_value = (SUCCESS204HEADERS, None)

        zoneid = uuid.uuid4()
        duration = randrange(10800)

        self.zone.start(zoneid, duration)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/zone/start")
        self.assertEqual(args[1], "PUT")
        self.assertEqual(kwargs["body"], {"id": zoneid, "duration": duration})

        # Check that values should be within range.
        self.assertRaises(AssertionError, self.zone.start, zoneid, -1)
        self.assertRaises(AssertionError, self.zone.start, zoneid, 10801)

    @patch("httplib2.Http.request")
    def test_start_multiple(self, mock):
        """Test if the start multiple method works as expected."""
        mock.return_value = (SUCCESS204HEADERS, None)
        zones = [
            {"id": data[0], "duration": data[1], "sortOrder": count}
            for (count, data) in enumerate(self.zones, 1)
        ]
        self.zone.start_multiple(zones)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/zone/start_multiple")
        self.assertEqual(args[1], "PUT")
        self.assertEqual(
            kwargs["body"],
            {
                "zones": [
                    {"id": data[0], "duration": data[1], "sortOrder": count}
                    for (count, data) in enumerate(self.zones, 1)
                ]
            },
        )

    @patch("httplib2.Http.request")
    def test_set_moisture_percent(self, mock):
        """Test if the set moisture percent method works as expected."""
        mock.return_value = (SUCCESS204HEADERS, None)

        zoneid = uuid.uuid4()
        percent = round(random.random(), 1)

        self.zone.set_moisture_percent(zoneid, percent)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/zone/setMoisturePercent")
        self.assertEqual(args[1], "PUT")
        self.assertEqual(kwargs["body"], {"id": zoneid, "percent": percent})

        # Check that values should be within range.
        self.assertRaises(
            AssertionError, self.zone.set_moisture_percent, zoneid, -0.1
        )
        self.assertRaises(
            AssertionError, self.zone.set_moisture_percent, zoneid, 1.1
        )

    @patch("httplib2.Http.request")
    def test_set_moisture_level(self, mock):
        """Test if the set moisture level method works as expected."""
        mock.return_value = (SUCCESS204HEADERS, None)

        zoneid = uuid.uuid4()
        level = round(random.uniform(0.0, 100.0), 2)

        self.zone.set_moisture_level(zoneid, level)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/zone/setMoistureLevel")
        self.assertEqual(args[1], "PUT")
        self.assertEqual(kwargs["body"], {"id": zoneid, "level": level})

    @patch("httplib2.Http.request")
    def test_zoneschedule(self, mock):
        """Test if the zoneschedule helper class works as expected."""
        mock.return_value = (SUCCESS204HEADERS, None)

        zoneschedule = self.zone.schedule()
        for zone in self.zones:
            zoneschedule.enqueue(zone[0], zone[1])
        zoneschedule.start()

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/zone/start_multiple")
        self.assertEqual(args[1], "PUT")
        self.assertEqual(
            kwargs["body"],
            {
                "zones": [
                    {"id": data[0], "duration": data[1], "sortOrder": count}
                    for (count, data) in enumerate(self.zones, 1)
                ]
            },
        )

    @patch("httplib2.Http.request")
    def test_zoneschedule_with_statement(self, mock):
        """Test if the zoneschedule with statement works as expected."""
        mock.return_value = (SUCCESS204HEADERS, None)

        with ZoneSchedule(self.zone) as zoneschedule:
            for zone in self.zones:
                zoneschedule.enqueue(zone[0], zone[1])

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[0], f"{BASE_API_URL}/zone/start_multiple")
        self.assertEqual(args[1], "PUT")
        self.assertEqual(
            kwargs["body"],
            {
                "zones": [
                    {"id": data[0], "duration": data[1], "sortOrder": count}
                    for (count, data) in enumerate(self.zones, 1)
                ]
            },
        )
