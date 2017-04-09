"""Notification module handling /notification/ API calls."""
#pylint: disable=invalid-name


class Notification(object):
    """Notification class with methods for /notification/ API calls."""
    def __init__(self, rachio):
        self.rachio = rachio

    def getWebhookEventType(self):
        """
        Retrieve the list of events types that are available to any webhook
        for subscription.
        """
        path = 'notification/webhook_event_type'
        return self.rachio.get(path)

    def getDeviceWebhook(self, dev_id):
        """Retrieve all webhooks for a device."""
        path = '/'.join(['notification', dev_id, 'webhook'])
        return self.rachio.get(path)

    def postWebhook(self, dev_id, external_id, url, event_types):
        """
        Add a webhook to a device. externalId can be used as opaque data that
        is tied to your company, and passed back in each webhook event
        response.
        """
        path = 'notification/webhook'
        payload = {'device': {'id': dev_id}, 'externalId': external_id,
                   'url': url, 'eventTypes': event_types}
        return self.rachio.post(path, payload)

    def putWebhook(self, hook_id, external_id, url, event_types):
        """Update a webhook."""
        path = 'notification/webhook'
        payload = {'id': hook_id, 'externalId': external_id,
                   'url': url, 'eventTypes': event_types}
        return self.rachio.put(path, payload)

    def deleteWebhook(self, hook_id):
        """Remove a webhook."""
        path = '/'.join(['notification', 'webhook', hook_id])
        return self.rachio.delete(path)

    def get(self, hook_id):
        """Get a webhook."""
        path = '/'.join(['notification', 'webhook', hook_id])
        return self.rachio.get(path)
