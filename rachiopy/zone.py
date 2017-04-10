"""Zone module handling /zone/ API calls."""
#pylint: disable=invalid-name


class Zone(object):
    """Zone class with methods for /zone/ API calls."""
    def __init__(self, rachio):
        self.rachio = rachio

    def start(self, zone_id, duration):
        """Start a zone."""
        path = 'zone/start'
        payload = {'id': zone_id, 'duration': duration}
        return self.rachio.put(path, payload)

    def startMultiple(self, zones):
        """Start multiple zones."""
        path = 'zone/start_multiple'
        payload = {'zones': zones}
        return self.rachio.put(path, payload)

    def schedule(self):
        """Create an empty zone schedule."""
        return ZoneSchedule(self)

    def get(self, zone_id):
        """Retrieve the information for a zone entity."""
        path = '/'.join(['zone', zone_id])
        return self.rachio.get(path)


class ZoneSchedule(object):
    """Help with starting multiple zones."""
    def __init__(self, zone_api):
        self._api = zone_api
        self._zones = []

    def enqueue(self, zone_id, duration):
        """Add a zone and duration to the schedule."""
        self._zones.append((zone_id, duration))

    def start(self):
        """Start the schedule."""
        zones = [{"id": data[0], "duration": data[1], "sortOrder": count}
                 for (count, data) in enumerate(self._zones, 1)]
        self._api.startMultiple(zones)

    def __enter__(self):
        """Allow a schedule to be created in a with block."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Allow the schedule to be executed by leaving with block."""
        self.start()
