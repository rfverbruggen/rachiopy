"""Flexschedulerule module handling /flexschedulerule/ API calls."""
#pylint: disable=invalid-name


class FlexSchedulerule(object):
    """
    FlexSchedulerule class with methods for /flexschedulerule/ API calls.
    """
    #pylint: disable=too-few-public-methods
    def __init__(self, rachio):
        self.rachio = rachio

    def get(self, flex_sched_rule_id):
        """Retrieve the information for a flexscheduleRule entity."""
        path = '/'.join(['flexschedulerule', flex_sched_rule_id])
        return self.rachio.get(path)
