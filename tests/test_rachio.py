"""Rachio basic test module"""

import unittest
from unittest.mock import patch, Mock
from rachiopy import Rachio


class TestRachioMethods(unittest.TestCase):
    """Class containing the basic test cases."""

    @patch('rachiopy.Person.get_info')
    def test_unauthorized(self, mock_get_info):
        """Test with invalid authtoken."""
        mock_get_info.return_value = Mock()
        mock_get_info.return_value.json = {
            "errors": [{"message": "The client is not authorized."}]
        }
        mock_get_info.return_value.status_code = 401

        rachio = Rachio("")
        response = rachio.person.get_info()

        assert response.status_code == 401
