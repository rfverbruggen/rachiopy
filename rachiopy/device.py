import json

class Device(object):
	def __init__(self, rachio):
		self.rachio = rachio

	def get(self, id):
		url = '%sdevice/%s' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

	def getCurrentSchedule(self, id):
		url = '%sdevice/%s/current_schedule' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

	def getEvent(self, id, starttime, endtime):
		url = '%sdevice/%s/event?startTime=%s&endTime=%s' % (self.rachio.server, id, starttime, endtime)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

	def getScheduleItem(self, id):
		url = '%sdevice/%s/scheduleitem' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

	def getForecast(self, id, units):
		url = '%s%sdevice/%s/forecast?units=%s' % (self.rachio.server, id, units)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

	def stopWater(self, id):
		url = '%sdevice/stop_water' % self.rachio.server
		payload = {'id' : id } 

		(resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), headers=self.rachio.headers)
		return (resp, content)

	def rainDelay(self, id, duration):
		url = '%sdevice/rain_delay' % self.rachio.server
		payload = { 'id' : id, 'duration' : duration }

		(resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), headers=self.rachio.headers)
		return (resp, content)

	def on(self, id):
		url = '%sdevice/on' % self.rachio.server
		payload = { 'id' : id }

		(resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), headers=self.rachio.headers)
		return (resp, content)

	def off(self, id):
		url = '%sdevice/off' % self.rachio.server
		payload = { 'id' : id }

		(resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), header=self.rachio.headers)
		return (resp, content) 
