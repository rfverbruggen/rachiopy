"""Main rachiopy module."""

from rachiopy.person import Person
from rachiopy.device import Device
from rachiopy.flexschedulerule import FlexSchedulerule
from rachiopy.notification import Notification
from rachiopy.schedulerule import Schedulerule
from rachiopy.zone import Zone


class Rachio():
    """Object representing the Rachio API."""

    def __init__(self, authtoken):
        """Initialze the Rachio API wrapper."""
        self.authtoken = authtoken
        self.person = Person(authtoken)
        self.device = Device(authtoken)
        self.flexschedulerule = FlexSchedulerule(authtoken)
        self.notification = Notification(authtoken)
        self.schedulerule = Schedulerule(authtoken)
        self.zone = Zone(authtoken)
