class Person(object):
	def __init__(self, rachio):
		self.rachio = rachio

	def getInfo(self):
		url = '%sperson/info' % (self.rachio.server)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

	def get(self, id):
		url = '%sperson/%s' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)
