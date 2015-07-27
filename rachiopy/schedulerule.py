class Schedulerule(object):
	def __init__(self, rachio):
		self.rachio = rachio

	def skip(self, id):
		url = '%sschedulerule/skip' % self.rachio.server
		body = { 'id' : id }

		(resp, content) = self.rachio.h.request(url, 'PUT', body=body, header=self.rachio.headers)
		return content

	def start(self, id):
		url = '%sschedulerule/start' % self.rachio.server
		body = { 'id': id }

		(resp, content) = self.rachio.h.request(url, 'PUT', body=body, headers=self.rachio.headers)
		return content

	def seasonalAdjustment(self, id, adjustment):
		url = '%sschedulerule/seasonal_adjustment' % self.rachio.server
		body = { 'id': id, 'adjustment': adjustment }

		(resp, content) = self.rachio.h.request(url, 'PUT', body=body, headers=self.rachio.headers)
		return content 
