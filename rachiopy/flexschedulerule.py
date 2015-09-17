class FlexSchedulerule(object):
	def __init__(self, rachio):
		self.rachio = rachio

	def get(self, id):
		url = '%sflexschedulerule/%s' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

