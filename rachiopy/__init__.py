"""Main rachiopy module."""

import json

from rachiopy.person import Person
from rachiopy.device import Device
from rachiopy.zone import Zone
from rachiopy.schedulerule import Schedulerule
from rachiopy.flexschedulerule import FlexSchedulerule
from rachiopy.notification import Notification

from requests import Session

_SERVER = "https://api.rach.io/1/public"


class Rachio(object):
    """Represent the Rachio API."""

    def __init__(self, authtoken, http_session=None):
        """Rachio class initializer."""
        self._headers = {'Content-Type': 'application/json',
                         'Authorization': 'Bearer %s' % authtoken}

        self.person = Person(self)
        self.device = Device(self)
        self.zone = Zone(self)
        self.schedulerule = Schedulerule(self)
        self.flexschedulerule = FlexSchedulerule(self)
        self.notification = Notification(self)
        self._http_session = http_session or Session()

    def _request(self, path, method, body=None):
        """Make a request from the API."""
        url = "/".join([_SERVER, path])
        response = self._http_session.request(
            method, url, headers=self._headers, data=body
        )

        content_type = response.headers.get("content-type")
        headers = {k.lower(): v for k, v in response.headers.items()}
        headers["status"] = response.status_code

        if content_type and content_type.startswith("application/json"):
            return headers, response.json()

        return headers, response.text

    def get(self, path):
        """Make a GET request from the API."""
        return self._request(path, 'GET')

    def delete(self, path):
        """Make a DELETE request from the API."""
        return self._request(path, 'DELETE')

    def put(self, path, payload):
        """Make a PUT request from the API."""
        body = json.dumps(payload)
        return self._request(path, 'PUT', body)

    def post(self, path, payload):
        """Make a POST request from the API."""
        body = json.dumps(payload)
        return self._request(path, 'POST', body)
