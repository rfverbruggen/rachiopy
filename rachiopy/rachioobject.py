"""RachioObject module containing a helper class for all API calls."""

import json
import httplib2

_API_URL = "https://api.rach.io/1/public"
_HTTP = httplib2.Http()


class RachioObject():
    """The Rachio base object."""

    def __init__(self, authtoken: str):
        """Rachioobject class initializer.

        :param authtoken: The API authentication token.
        :type authtoken: str
        """
        self.authtoken = authtoken
        self._headers = {"Content-Type": "application/json",
                         "Authorization": f"Bearer {authtoken}"}

    def _request(self, path, method, body=None):
        """Make a request from the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        url = f"{_API_URL}/{path}"
        (resp, content) = _HTTP.request(url, method,
                                        headers=self._headers, body=body)

        content_type = resp.get("content-type")
        if content_type and content_type.startswith("application/json"):
            content = json.loads(content.decode("UTF-8"))

        return (resp, content)

    def get_request(self, path, body=None):
        """Make a GET request to the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        return self._request(path, "GET", body)

    def put_request(self, path, body=None):
        """Make a PUT request to the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        return self._request(path, "PUT", body)

    def post_request(self, path, body=None):
        """Make a POST request to the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        return self._request(path, "POST", body)

    def delete_request(self, path, body=None):
        """Make a DELETE request to the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        return self._request(path, "DELETE", body)
