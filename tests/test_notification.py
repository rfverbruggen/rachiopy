"""Notification object test module"""

import unittest
from unittest.mock import patch
import uuid
import json

from rachiopy import Notification
from tests.constants import BASE_API_URL, AUTHTOKEN, RESPONSE200, RESPONSE204


class TestNotificationMethods(unittest.TestCase):
    """Class containing the Notification object test cases."""

    def setUp(self):
        self.notification = Notification(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.notification.authtoken, AUTHTOKEN)

    @patch("requests.Session.request")
    def test_get_webhook_eventtype(self, mock):
        """Test if the get webhook eventtype method works as expected."""
        mock.return_value = RESPONSE200

        self.notification.get_webhook_event_type()

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{BASE_API_URL}/notification/webhook_event_type"
        )
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_get_device_webhook(self, mock):
        """Test if the get device webhook method works as expected."""
        mock.return_value = RESPONSE200

        deviceid = str(uuid.uuid4())

        self.notification.get_device_webhook(deviceid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{BASE_API_URL}/notification/" f"{deviceid}/webhook"
        )
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_add(self, mock):
        """Test if the add method works as expected."""
        mock.return_value = RESPONSE200

        deviceid = str(uuid.uuid4())
        externalid = "Test ID"
        url = "https://www.mydomain.com/another_webhook_new_url"
        eventtypes = [{"id": "1"}, {"id": "2"}]

        self.notification.add(deviceid, externalid, url, eventtypes)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{BASE_API_URL}/notification/webhook")
        self.assertEqual(args[0], "POST")
        self.assertEqual(
            kwargs["data"],
            json.dumps(
                {
                    "device": {"id": deviceid},
                    "externalId": externalid,
                    "url": url,
                    "eventTypes": eventtypes,
                }
            ),
        )

    @patch("requests.Session.request")
    def test_update(self, mock):
        """Test if the update method works as expected."""
        mock.return_value = RESPONSE200

        hookid = str(uuid.uuid4())
        externalid = "Test ID"
        url = "https://www.mydomain.com/another_webhook_new_url"
        eventtypes = [{"id": "1"}, {"id": "2"}]

        self.notification.update(hookid, externalid, url, eventtypes)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{BASE_API_URL}/notification/webhook")
        self.assertEqual(args[0], "PUT")
        self.assertEqual(
            kwargs["data"],
            json.dumps(
                {
                    "id": hookid,
                    "externalId": externalid,
                    "url": url,
                    "eventTypes": eventtypes,
                }
            ),
        )

    @patch("requests.Session.request")
    def test_delete(self, mock):
        """Test if the delete method works as expected."""
        mock.return_value = RESPONSE204

        hookid = str(uuid.uuid4())

        self.notification.delete(hookid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{BASE_API_URL}/notification/webhook/" f"{hookid}"
        )
        self.assertEqual(args[0], "DELETE")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_get(self, mock):
        """Test if the get method works as expected."""
        mock.return_value = RESPONSE200

        hookid = str(uuid.uuid4())

        self.notification.get(hookid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(
            args[1], f"{BASE_API_URL}/notification/webhook/" f"{hookid}"
        )
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)
