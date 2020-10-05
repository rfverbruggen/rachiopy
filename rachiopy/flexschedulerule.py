"""Flexschedulerule module handling /flexschedulerule/ API calls."""

from rachiopy.rachioobject import RachioObject


class FlexSchedulerule(RachioObject):
    """FlexSchedulerule class with methods for /flexschedulerule/ calls."""

    def get(self, flex_sched_rule_id: str):
        """Retrieve the information for a flexscheduleRule entity.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicflexscheduleruleid

        :param flex_sched_rule_id: FlexScheduleRule's unique id
        :type flex_sched_rule_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        path = f"flexschedulerule/{flex_sched_rule_id}"
        return self.get_request(path)
