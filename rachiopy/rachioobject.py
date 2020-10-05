"""RachioObject module containing a helper class for all API calls."""

from requests import Session

_API_URL = "https://api.rach.io/1/public"


class RachioObject:
    """The Rachio base object."""

    def __init__(self, authtoken: str, http_session=None):
        """Rachioobject class initializer.

        :param authtoken: The API authentication token.
        :type authtoken: str

        :param http_session: The HTTP Session
        :type http_session: Session
        """
        self.authtoken = authtoken
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authtoken}",
        }
        self._http_session = http_session or Session()

    def _request(self, path: str, method: str, body=None):
        """Make a request from the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        url = f"{_API_URL}/{path}"
        response = self._http_session.request(
            method, url, headers=self._headers, data=body
        )

        content_type = response.headers.get("content-type")
        headers = {k.lower(): v for k, v in response.headers.items()}
        headers["status"] = response.status_code

        if content_type and content_type.startswith("application/json"):
            return headers, response.json()

        return headers, response.text

    def get_request(self, path: str, body=None):
        """Make a GET request to the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        return self._request(path, "GET", body)

    def put_request(self, path: str, body=None):
        """Make a PUT request to the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        return self._request(path, "PUT", body)

    def post_request(self, path: str, body=None):
        """Make a POST request to the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        return self._request(path, "POST", body)

    def delete_request(self, path: str, body=None):
        """Make a DELETE request to the API.

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        return self._request(path, "DELETE", body)
