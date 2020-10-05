"""Schedulerule module handling /scheduerule/ API calls."""

from decimal import Decimal

from rachiopy.rachioobject import RachioObject


class Schedulerule(RachioObject):
    """Schedulerule class with methods for /schedulerule/ API calls."""

    def skip(self, sched_rule_id: str):
        """Skip a schedule rule (watering time).

        For more info of the content in the response see:
        https://rachio.readme.io/docs/scheduleruleskip

        :param sched_rule_id: Schedule rule's unique id
        :type sched_rule_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        payload = {"id": sched_rule_id}
        return self.put_request("schedulerule/skip", payload)

    def start(self, sched_rule_id: str):
        """Start a schedule rule (watering time).

        For more info of the content in the response see:
        https://rachio.readme.io/docs/schedulerulestart

        :param sched_rule_id: Schedule rule's unique id
        :type sched_rule_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        payload = {"id": sched_rule_id}
        return self.put_request("schedulerule/start", payload)

    def seasonal_adjustment(self, sched_rule_id: str, adjustment: Decimal):
        """Seasonal adjustment for a schedule rule (watering time).

        This adjustment amount will be applied to the overall run time of the
        selected schedule while overriding any current adjustments.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicscheduleruleseasonal_adjustment

        :param sched_rule_id: Schedule rule's unique id
        :type sched_rule_id: str

        :param adjustment: Seasonal adjustment percent from 100% to -100%
            (valid data range is 1 to -1)
        :type adjustment: Decimal

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        payload = {"id": sched_rule_id, "adjustment": adjustment}
        return self.put_request("schedulerule/seasonal_adjustment", payload)

    def get(self, sched_rule_id: str):
        """Retrieve the information for a scheduleRule entity.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicscheduleruleid

        :param sched_rule_id: Schedule rule's unique id
        :type sched_rule_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        path = f"schedulerule/{sched_rule_id}"
        return self.get_request(path)
