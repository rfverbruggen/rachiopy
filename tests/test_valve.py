"""Valve object test module"""

import unittest
from unittest.mock import patch
import uuid
import json

from random import randrange
from rachiopy import Valve
from tests.constants import VALVE_API_URL, AUTHTOKEN, RESPONSE200, RESPONSE204


class TestValveMethods(unittest.TestCase):
    """Class containing the Valve object test cases."""

    def setUp(self):
        self.valve = Valve(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.valve.authtoken, AUTHTOKEN)

    @patch("requests.Session.request")
    def test_get_valve(self, mock):
        """Test if the get_valve method works as expected."""
        mock.return_value = RESPONSE200

        valveid = uuid.uuid4()

        self.valve.get_valve(valveid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{VALVE_API_URL}/valve/getValve/{valveid}")
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_get_base_station(self, mock):
        """Test if the get_base_station method works as expected."""
        mock.return_value = RESPONSE200

        baseid = str(uuid.uuid4())

        self.valve.get_base_station(baseid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1],
            f"{VALVE_API_URL}/valve/getBaseStation/{baseid}"
            )
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_list_base_stations(self, mock):
        """Test if the list_base_stations method works as expected."""
        mock.return_value = RESPONSE200

        userid = str(uuid.uuid4())

        self.valve.list_base_stations(userid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1],
            f"{VALVE_API_URL}/valve/listBaseStations/{userid}"
            )
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_list_valves(self, mock):
        """Test if the list_valves method works as expected."""
        mock.return_value = RESPONSE200

        baseid = str(uuid.uuid4())

        self.valve.list_valves(baseid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{VALVE_API_URL}/valve/listValves/{baseid}")
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_set_default_runtime(self, mock):
        """Test if the set_default_runtime method works as expected."""
        mock.return_value = RESPONSE200

        valveid = str(uuid.uuid4())
        duration = randrange(86400)

        self.valve.set_default_runtime(valveid, duration)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{VALVE_API_URL}/valve/setDefaultRuntime")
        self.assertEqual(args[0], "PUT")
        self.assertEqual(
            kwargs["data"],
            json.dumps({"valveId": valveid, "defaultRuntimeSeconds": duration})
        )

        # Check that values should be within range.
        self.assertRaises(
            AssertionError, self.valve.start_watering, valveid, -1
            )
        self.assertRaises(
            AssertionError, self.valve.start_watering, valveid, 86401
            )

    @patch("requests.Session.request")
    def test_start_watering(self, mock):
        """Test if the start_watering method works as expected."""
        mock.return_value = RESPONSE204

        valveid = str(uuid.uuid4())
        duration = randrange(86400)

        self.valve.start_watering(valveid, duration)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{VALVE_API_URL}/valve/startWatering")
        self.assertEqual(args[0], "PUT")
        self.assertEqual(
            kwargs["data"],
            json.dumps({"valveId": valveid, "durationSeconds": duration})
        )

        # Check that values should be within range.
        self.assertRaises(
            AssertionError, self.valve.start_watering, valveid, -1
            )
        self.assertRaises(
            AssertionError, self.valve.start_watering, valveid, 86401
            )

    @patch("requests.Session.request")
    def test_stop_watering(self, mock):
        """Test if the stop_watering method works as expected."""
        mock.return_value = RESPONSE204

        valveid = str(uuid.uuid4())

        self.valve.stop_watering(valveid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{VALVE_API_URL}/valve/stopWatering")
        self.assertEqual(args[0], "PUT")
        self.assertEqual(
            kwargs["data"], json.dumps({"valveId": valveid})
        )
