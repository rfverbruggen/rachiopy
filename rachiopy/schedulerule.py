"""Schedulerule module handling /scheduerule/ API calls."""

from rachiopy.rachioobject import RachioObject


class Schedulerule(RachioObject):
    """Schedulerule class with methods for /schedulerule/ API calls."""

    def skip(self, sched_rule_id):
        """Skip a schedule rule (watering time)."""
        payload = {"id": sched_rule_id}
        return self.put_request("schedulerule/skip", payload)

    def start(self, sched_rule_id):
        """Start a schedule rule (watering time)."""
        payload = {"id": sched_rule_id}
        return self.put_request("schedulerule/start", payload)

    def seasonal_adjustment(self, sched_rule_id, adjustment):
        """Seasonal adjustment for a schedule rule (watering time).

        This adjustment amount will be applied to the overall run time of the
        selected schedule while overriding any current adjustments.
        """
        payload = {"id": sched_rule_id, "adjustment": adjustment}
        return self.put_request("schedulerule/seasonal_adjustment", payload)

    def get(self, sched_rule_id):
        """Retrieve the information for a scheduleRule entity."""
        path = f"schedulerule/{sched_rule_id}"
        return self.get_request(path)
