"""Notification module handling /notification/ API calls."""

from rachiopy.rachioobject import RachioObject


class Notification(RachioObject):
    """Notification class with methods for /notification/ API calls."""

    def get_webhook_event_type(self):
        """Retrieve the list of events types.

        Event types that are available to any webhook for subscription.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicnotificationwebhook_event_type

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        return self.get_request("notification/webhook_event_type")

    def get_device_webhook(self, dev_id: str):
        """Retrieve all webhooks for a device.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicnotificationdeviceidwebhook

        :param dev_id: Device's unique id
        :type dev_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        path = f"notification/{dev_id}/webhook"
        return self.get_request(path)

    def add(self, dev_id: str, external_id: str, url: str, event_types):
        """Add a webhook to a device.

        externalId can be used as opaque data that
        is tied to your company, and passed back in each webhook event
        response.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicnotificationwebhook

        :param dev_id: Device's unique id
        :type dev_id: str

        :param external_id: External company ID
        :type exteranl_id: str

        :param url: External webhook URL
        :type url: str

        :param event_type: Event types
        :type event_type: Object[]

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        payload = {
            "device": {"id": dev_id},
            "externalId": external_id,
            "url": url,
            "eventTypes": event_types,
        }
        return self.post_request("notification/webhook", payload)

    def update(self, hook_id: str, external_id: str, url: str, event_types):
        """Update a webhook.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicnotificationwebhook-1

        :param hook_id: Webhook's unique id
        :type hook_id: str

        :param external_id: External company ID
        :type exteranl_id: str

        :param url: External webhook URL
        :type url: str

        :param event_type: Event types
        :type event_type: Object[]

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        payload = {
            "id": hook_id,
            "externalId": external_id,
            "url": url,
            "eventTypes": event_types,
        }
        return self.put_request("notification/webhook", payload)

    def delete(self, hook_id: str):
        """Remove a webhook.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicnotificationwebhookid

        :param hook_id: Webhook's unique id
        :type hook_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        path = f"notification/webhook/{hook_id}"
        return self.delete_request(path)

    def get(self, hook_id: str):
        """Get a webhook.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicnotificationdeviceidwebhook

        :param hook_id: Webhook's unique id
        :type hook_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        path = f"notification/webhook/{hook_id}"
        return self.get_request(path)
