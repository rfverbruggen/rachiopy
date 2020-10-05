"""Main rachiopy module."""

from rachiopy.rachioobject import RachioObject
from rachiopy.person import Person
from rachiopy.device import Device
from rachiopy.flexschedulerule import FlexSchedulerule
from rachiopy.notification import Notification
from rachiopy.schedulerule import Schedulerule
from rachiopy.zone import Zone


class Rachio(RachioObject):
    """Object representing the Rachio API."""

    def __init__(self, authtoken: str):
        """Initialze the Rachio API wrapper.

        :param authtoken: The API authentication token.
        :type authtoken: str
        """
        super().__init__(authtoken)
        self.person = Person(authtoken)
        self.device = Device(authtoken)
        self.flexschedulerule = FlexSchedulerule(authtoken)
        self.notification = Notification(authtoken)
        self.schedulerule = Schedulerule(authtoken)
        self.zone = Zone(authtoken)
