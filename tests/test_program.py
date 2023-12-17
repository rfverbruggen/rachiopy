"""Program object test module"""

import unittest
import uuid
import json
from unittest.mock import patch

from rachiopy import Program
from tests.constants import VALVE_API_URL, AUTHTOKEN, RESPONSE200


class TestProgramMethods(unittest.TestCase):
    """Class containing the Program object tests."""

    def setUp(self):
        self.program = Program(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.program.authtoken, AUTHTOKEN)

    @patch("requests.Session.request")
    def test_list_programs(self, mock):
        """Test if the list programs method works as expected."""
        mock.return_value = RESPONSE200

        valveid = str(uuid.uuid4())

        self.program.list_programs(valveid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{VALVE_API_URL}/program/listPrograms/{valveid}"
        )
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_get_program(self, mock):
        """Test if the get program method works as expected."""
        mock.return_value = RESPONSE200

        programid = str(uuid.uuid4())

        self.program.get_program(programid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{VALVE_API_URL}/program/getProgram/{programid}"
        )
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_create_skip_overrides(self, mock):
        """Test if the create skip overrides method works as expected."""
        mock.return_value = RESPONSE200

        programid = str(uuid.uuid4())
        timestamp = 1414818000000

        self.program.create_skip_overrides(programid, timestamp)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{VALVE_API_URL}/program/createSkipOverrides"
        )
        self.assertEqual(args[0], "POST")
        self.assertEqual(
            kwargs["data"],
            json.dumps({"programId": programid, "timestamp": timestamp}),
        )

    @patch("requests.Session.request")
    def test_delete_skip_overrides(self, mock):
        """Test if the delete skip overrides method works as expected."""
        mock.return_value = RESPONSE200

        programid = str(uuid.uuid4())
        timestamp = 1414818000000

        self.program.delete_skip_overrides(programid, timestamp)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{VALVE_API_URL}/program/deleteSkipOverrides"
        )
        self.assertEqual(args[0], "POST")
        self.assertEqual(
            kwargs["data"],
            json.dumps({"programId": programid, "timestamp": timestamp}),
        )
