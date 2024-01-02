"""Constants for test execution."""

from unittest.mock import Mock

from requests import Response

BASE_API_URL = "https://api.rach.io/1/public"
VALVE_API_URL = "https://cloud-rest.rach.io"

AUTHTOKEN = "1c1d9f3d-39c9-42b1-abc0-066f5a05cdef"

RESPONSE200 = Mock(spec=Response)
RESPONSE200.status_code = 200
RESPONSE200.headers = {"content-type": "application/json"}
RESPONSE200.json.return_value = {}

RESPONSE204 = Mock(spec=Response)
RESPONSE204.headers = {}
RESPONSE204.status_code = 204
