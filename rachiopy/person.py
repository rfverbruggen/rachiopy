"""Person module handling /person/ API calls."""
#pylint: disable=invalid-name


class Person(object):
    """Person class with methods for /person/ API calls."""
    def __init__(self, rachio):
        self.rachio = rachio

    def getInfo(self):
        """
        Retrieve the id for the person entity currently logged in
        through OAuth.
        """
        path = 'person/info'
        return self.rachio.get(path)

    def get(self, user_id):
        """Retrieve the information for a person entity."""
        path = '/'.join(['person', user_id])
        return self.rachio.get(path)
