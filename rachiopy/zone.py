"""Zone module handling /zone/ API calls."""

from rachiopy.rachioobject import RachioObject


class Zone(RachioObject):
    """Zone class with methods for /zone/ API calls."""

    def start(self, zone_id, duration):
        """Start a zone."""
        assert 0 <= duration <= 10800, "duration must be in range 0-10800"
        payload = {"id": zone_id, "duration": duration}
        return self.put_request("zone/start", payload)

    def start_multiple(self, zones):
        """Start multiple zones."""
        payload = {"zones": zones}
        return self.put_request("zone/start_multiple", payload)

    def schedule(self):
        """Create an empty zone schedule."""
        return ZoneSchedule(self)

    def set_moisture_percent(self, zone_id, percent):
        """Set zone moisture percent."""
        assert 0 <= percent <= 1, "percent must be in range 0.0-1.0"
        payload = {"id": zone_id, "percent": percent}
        return self.put_request("zone/setMoisturePercent", payload)

    def set_moisture_level(self, zone_id, level):
        """Set zone moisture level."""
        payload = {"id": zone_id, "level": level}
        return self.put_request("zone/setMoistureLevel", payload)

    def get(self, zone_id):
        """Retrieve the information for a zone entity."""
        path = f"zone/{zone_id}"
        return self.get_request(path)


class ZoneSchedule:
    """Help with starting multiple zones."""

    def __init__(self, zone_api):
        """Zoneschedule class initializer."""
        self._api = zone_api
        self._zones = []

    def enqueue(self, zone_id, duration):
        """Add a zone and duration to the schedule."""
        self._zones.append((zone_id, duration))

    def start(self):
        """Start the schedule."""
        zones = [
            {"id": data[0], "duration": data[1], "sortOrder": count}
            for (count, data) in enumerate(self._zones, 1)
        ]
        self._api.start_multiple(zones)

    def __enter__(self):
        """Allow a schedule to be created in a with block."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Allow the schedule to be executed by leaving with block."""
        self.start()
