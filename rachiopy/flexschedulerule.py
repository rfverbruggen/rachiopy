"""Flexschedulerule module handling /flexschedulerule/ API calls."""


# pylint: disable=invalid-name
# pylint: disable=useless-object-inheritance
# pylint: disable=too-few-public-methods
class FlexSchedulerule(object):
    """FlexSchedulerule class with methods for /flexschedulerule/ calls."""

    def __init__(self, rachio):
        """Flexschedulerule class initializer."""
        self.rachio = rachio

    def get(self, flex_sched_rule_id):
        """Retrieve the information for a flexscheduleRule entity."""
        path = '/'.join(['flexschedulerule', flex_sched_rule_id])
        return self.rachio.get(path)
