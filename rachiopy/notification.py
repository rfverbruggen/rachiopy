"""Notification module handling /notification/ API calls."""

from rachiopy.rachioobject import RachioObject


class Notification(RachioObject):
    """Notification class with methods for /notification/ API calls."""

    def get_webhook_event_type(self):
        """Retrieve the list of events types.

        Event types that are available to any webhook for subscription.
        """
        return self.get_request("notification/webhook_event_type")

    def get_device_webhook(self, dev_id):
        """Retrieve all webhooks for a device."""
        path = f"notification/{dev_id}/webhook"
        return self.get_request(path)

    def add(self, dev_id, external_id, url, event_types):
        """Add a webhook to a device.

        externalId can be used as opaque data that
        is tied to your company, and passed back in each webhook event
        response.
        """
        payload = {
            "device": {"id": dev_id},
            "externalId": external_id,
            "url": url,
            "eventTypes": event_types,
        }
        return self.post_request("notification/webhook", payload)

    def update(self, hook_id, external_id, url, event_types):
        """Update a webhook."""
        payload = {
            "id": hook_id,
            "externalId": external_id,
            "url": url,
            "eventTypes": event_types,
        }
        return self.put_request("notification/webhook", payload)

    def delete(self, hook_id):
        """Remove a webhook."""
        path = f"notification/webhook/{hook_id}"
        return self.delete_request(path)

    def get(self, hook_id):
        """Get a webhook."""
        path = f"notification/webhook/{hook_id}"
        return self.get_request(path)
