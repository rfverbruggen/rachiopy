"""Device module handling /device/ API calls."""


class Device(object):
    """Device class with /device/ API calls."""

    def __init__(self, rachio):
        """Device class initializer."""
        self.rachio = rachio

    def get(self, dev_id):
        """Retrieve the information for a device entity."""
        path = '/'.join(['device', dev_id])
        return self.rachio.get(path)

    def getCurrentSchedule(self, dev_id):
        """Retrieve current schedule running, if any."""
        path = '/'.join(['device', dev_id, 'current_schedule'])
        return self.rachio.get(path)

    def getEvent(self, dev_id, starttime, endtime):
        """Retrieve events for a device entity."""
        path = 'device/%s/event?startTime=%s&endTime=%s' % \
            (dev_id, starttime, endtime)
        return self.rachio.get(path)

    def getScheduleItem(self, dev_id):
        """Retrieve the next two weeks of schedule items for a device."""
        path = '/'.join(['device', dev_id, 'scheduleitem'])
        return self.rachio.get(path)

    def getForecast(self, dev_id, units):
        """Retrieve current and predicted forecast."""
        assert units in ['US', 'METRIC'], 'units must be either US or METRIC'
        path = 'device/%s/forecast?units=%s' % (dev_id, units)
        return self.rachio.get(path)

    def stopWater(self, dev_id):
        """Stop all watering on device."""
        path = 'device/stop_water'
        payload = {'id': dev_id}
        return self.rachio.put(path, payload)

    def rainDelay(self, dev_id, duration):
        """Rain delay device."""
        path = 'device/rain_delay'
        payload = {'id': dev_id, 'duration': duration}
        return self.rachio.put(path, payload)

    def on(self, dev_id):
        """Turn ON all features of the device.

        schedules, weather intelligence, water budget, etc.
        """
        path = 'device/on'
        payload = {'id': dev_id}
        return self.rachio.put(path, payload)

    def off(self, dev_id):
        """Turn OFF all features of the device.

        schedules, weather intelligence, water budget, etc.
        """
        path = 'device/off'
        payload = {'id': dev_id}
        return self.rachio.put(path, payload)

    def pauseZoneRun(self, dev_id, duration):
        """Pause currently running zone."""
        path = 'device/pause_zone_run'
        payload = {'id': dev_id, 'duration': duration}
        return self.rachio.put(path, payload)

    def resumeZoneRun(self, dev_id):
        """Resume paused zone."""
        path = 'device/resume_zone_run'
        payload = {'id': dev_id}
        return self.rachio.put(path, payload)
