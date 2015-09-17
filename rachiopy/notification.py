import json

class Notification(object):
	def __init__(self, rachio):
		self.rachio = rachio

	def getWebhookEventType(self):
		url = '%snotification/webhook_event_type' % self.rachio.server

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

	def getDeviceWebhook(self, id):
		url = '%snotification/%s/webhook' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)

	def postWebhook(self, webhook):
		url = '%snotification/webhook' % self.rachio.server
		payload = {webhook}

		(resp, content) = self.rachio.h.request(url, 'POST', body=json.dumps(payload), headers=self.rachio.headers)
		return (resp, content)

	def putWebhook(self, webhook):
		url = '%snotification/webhook' % self.rachio.server
		payload = {webhook}

		(resp, content) = self.rachio.h.request(url, 'PUT', body=json.dumps(payload), headers=self.rachio.headers)
		return (resp, content)

	def deleteWebhook(self, id):
		url = '%snotification/webhook/%s' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'DELETE', headers=self.rachio.headers)
		return (resp, content)

	def get(self, id):
		url = '%snotification/webhook/%s' % (self.rachio.server, id)

		(resp, content) = self.rachio.h.request(url, 'GET', headers=self.rachio.headers)
		return (resp, content)
