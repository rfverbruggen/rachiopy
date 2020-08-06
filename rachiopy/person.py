"""Person module handling /person/ API calls."""

from rachiopy.rachioobject import RachioObject


class Person(RachioObject):
    """Person class with methods for /person/ API calls."""

    def get_info(self):
        """Retrieve the id for the person entity currently logged in."""
        return self.get_request("person/info")

    def get(self, user_id):
        """Retrieve the information for a person entity."""
        path = f"person/{user_id}"
        return self.get_request(path)
