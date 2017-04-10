"""Schedulerule module handling /scheduerule/ API calls."""
#pylint: disable=invalid-name


class Schedulerule(object):
    """Schedulerule class with methods for /schedulerule/ API calls."""
    def __init__(self, rachio):
        self.rachio = rachio

    def skip(self, sched_rule_id):
        """Skip a schedule rule (watering time)."""
        path = 'schedulerule/skip'
        payload = {'id' : sched_rule_id}
        return self.rachio.put(path, payload)

    def start(self, sched_rule_id):
        """Start a schedule rule (watering time)."""
        path = 'schedulerule/start'
        payload = {'id': sched_rule_id}
        return self.rachio.put(path, payload)

    def seasonalAdjustment(self, sched_rule_id, adjustment):
        """
        Seasonal adjustment for a schedule rule (watering time). This
        adjustment amount will be applied to the overall run time of the
        selected schedule while overriding any current adjustments.
        """
        path = 'schedulerule/seasonal_adjustment'
        payload = {'id': sched_rule_id, 'adjustment': adjustment}
        return self.rachio.put(path, payload)

    def get(self, sched_rule_id):
        """Retrieve the information for a scheduleRule entity."""
        path = '/'.join(['schedulerule', sched_rule_id])
        return self.rachio.get(path)
