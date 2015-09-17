import json 

class Schedulerule(object):
	def __init__(self, rachio):
		self.rachio = rachio

	def skip(self, id):
		url = '%sschedulerule/skip' % self.rachio.server
		payload = { 'id' : id }

		(resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), header=self.rachio.headers)
		return (resp, content)

	def start(self, id):
		url = '%sschedulerule/start' % self.rachio.server
		payload = { 'id': id }

		(resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), headers=self.rachio.headers)
		return (resp, content)

	def seasonalAdjustment(self, id, adjustment):
		url = '%sschedulerule/seasonal_adjustment' % self.rachio.server
		payload = { 'id': id, 'adjustment': adjustment }

		(resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), headers=self.rachio.headers)
		return (resp, content)

	def get(self, id):
		url = '%sschedulerule/%s' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

