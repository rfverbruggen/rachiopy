"""Person module handling /person/ API calls."""

from rachiopy.rachioobject import RachioObject


class Person(RachioObject):
    """Person class with methods for /person/ API calls."""

    def info(self):
        """Retrieve the id for the person entity currently logged in.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicpersoninfo

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        return self.get_request("person/info")

    def get(self, user_id: str):
        """Retrieve the information for a person entity.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicpersonid

        :param user_id: Person's unique id
        :type user_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"person/{user_id}"
        return self.get_request(path)
