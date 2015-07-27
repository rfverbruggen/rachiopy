class Notification(object):
	def __init__(self, rachio):
		self.rachio = rachio

	def getWebhookEventType(self):
		url = '%snotification/webhook_event_type' % self.rachio.server

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return content

	def getDeviceWebhook(self, id):
		url = '%snotification/%s/webhook' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return content

	def postWebhook(self, webhook):
		url = '%snotification/webhook' % self.rachio.server
		body = {webhook}

		(resp, content) = self.rachio.h.request(url, 'POST', body=body, headers=self.rachio.headers)
		return content

	def putWebhook(self, webhook):
		url = '%snotification/webhook' % self.rachio.server
		body = {webhook}

		(resp, content) = self.rachio.h.request(url, 'PUT', body=body, headers=self.rachio.headers)
		return content

	def deleteWebhook(self, id):
		url = '%snotification/webhook/%s' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'DELETE', headers=self.rachio.headers)
		return content  
