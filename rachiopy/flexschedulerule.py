"""Flexschedulerule module handling /flexschedulerule/ API calls."""

from rachiopy.rachioobject import RachioObject


class FlexSchedulerule(RachioObject):
    """FlexSchedulerule class with methods for /flexschedulerule/ calls."""

    def get(self, flex_sched_rule_id):
        """Retrieve the information for a flexscheduleRule entity."""
        path = f"flexschedulerule/{flex_sched_rule_id}"
        return self.get_request(path)
