import httplib2

from person import Person
from device import Device
from zone import Zone
from schedulerule import Schedulerule
from flexschedulerule import FlexSchedulerule
from notification import Notification

class Rachio(object):
	def __init__(self, authtoken):
		self.server = 'https://api.rach.io/1/public/'
		self.headers = {
			'Content-Type': 'application/json',
			'Authorization': 'Bearer %s' % authtoken
			}
		self.h = httplib2.Http('.cache')

		self.person = Person(self)
		self.device = Device(self)
		self.zone = Zone(self)
		self.schedulerule = Schedulerule(self)
		self.flexschedulerule = FlexSchedulerule(self)
		self.notification = Notification(self)
