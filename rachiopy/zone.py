class Zone(object):
	def __init__(self, rachio):
		self.rachio = rachio

	def start(self, id, duration):
		url = '%szone/start' % rachio.server
		body = { 'id' : id, 'duration' : duration }

		(resp, content) = rachio.h.request(url, 'PUT', body=body, headers=rachio.headers)
		return content

	def startMultiple(self, zones):
		url = '%szone/start_multiple' % rachio.server
		body = { 'zones': zones }

		(resp, content) = rachio.h.request(url, 'PUT', headers=rachio.headers)
		return content 
