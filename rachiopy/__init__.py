"""Main rachiopy module"""

import json
import httplib2

from rachiopy.person import Person
from rachiopy.device import Device
from rachiopy.zone import Zone
from rachiopy.schedulerule import Schedulerule
from rachiopy.flexschedulerule import FlexSchedulerule
from rachiopy.notification import Notification

_SERVER = 'https://api.rach.io/1/public'
_HTTP = httplib2.Http()

#pylint: disable=too-many-instance-attributes
class Rachio(object):
    """Represent the Rachio API."""
    def __init__(self, authtoken):
        self._headers = {'Content-Type': 'application/json',
                         'Authorization': 'Bearer %s' % authtoken}

        self.person = Person(self)
        self.device = Device(self)
        self.zone = Zone(self)
        self.schedulerule = Schedulerule(self)
        self.flexschedulerule = FlexSchedulerule(self)
        self.notification = Notification(self)

    def _request(self, path, method, body=None):
        """Make a request from the API."""
        url = '/'.join([_SERVER, path])
        (resp, content) = _HTTP.request(url, method,
                                        headers=self._headers, body=body)

        content_type = resp.get('content-type')
        if content_type and content_type.startswith('application/json'):
            content = json.loads(content.decode('UTF-8'))

        return (resp, content)

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
