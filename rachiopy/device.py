"""Device module handling /device/ API calls."""

from rachiopy.rachioobject import RachioObject


class Device(RachioObject):
    """Device class with /device/ API calls."""

    def get(self, dev_id):
        """Retrieve the information for a device entity."""
        path = f"device/{dev_id}"
        return self.get_request(path)

    def get_current_schedule(self, dev_id):
        """Retrieve current schedule running, if any."""
        path = f"device/{dev_id}/current_schedule"
        return self.get_request(path)

    def get_event(self, dev_id, starttime, endtime):
        """Retrieve events for a device entity."""
        path = f"device/{dev_id}/event?startTime={starttime}&endTime={endtime}"
        return self.get_request(path)

    def get_schedule_item(self, dev_id):
        """Retrieve the next two weeks of schedule items for a device."""
        path = f"device/{dev_id}/scheduleitem"
        return self.get_request(path)

    def get_forecast(self, dev_id, units):
        """Retrieve current and predicted forecast."""
        assert units in ['US', 'METRIC'], 'units must be either US or METRIC'
        path = f"device/{dev_id}/forecast?units={units}"
        return self.get_request(path)

    def stop_water(self, dev_id):
        """Stop all watering on device."""
        payload = {"id": dev_id}
        return self.put_request("device/stop_water", payload)

    def set_rain_delay(self, dev_id, duration):
        """Rain delay device."""
        payload = {"id": dev_id, "duration": duration}
        return self.put_request("device/rain_delay", payload)

    def turn_on(self, dev_id):
        """Turn ON all features of the device.

        schedules, weather intelligence, water budget, etc.
        """
        payload = {"id": dev_id}
        return self.put_request("device/on", payload)

    def turn_off(self, dev_id):
        """Turn OFF all features of the device.

        schedules, weather intelligence, water budget, etc.
        """
        payload = {"id": dev_id}
        return self.put_request("device/off", payload)
