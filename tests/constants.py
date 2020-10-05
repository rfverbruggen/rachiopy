"""Constants for test execution."""

import json
from httplib2 import Response

BASE_API_URL = "https://api.rach.io/1/public"

AUTHTOKEN = "1c1d9f3d-39c9-42b1-abc0-066f5a05cdef"

SUCCESS200HEADERS = Response(
    {"status": 200, "content-type": "application/json"}
)
SUCCESS204HEADERS = Response({"status": 204})

JSONBODY = json.dumps({}).encode()
