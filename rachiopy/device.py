"""Device module handling /device/ API calls."""

from rachiopy.rachioobject import RachioObject


class Device(RachioObject):
    """Device class with /device/ API calls."""

    def get(self, dev_id: str):
        """Retrieve the information for a device entity.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicdeviceid

        :param dev_id: Device's unique id
        :type dev_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"device/{dev_id}"
        return self.get_request(path)

    def current_schedule(self, dev_id: str):
        """Retrieve current schedule running, if any.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicdeviceidcurrent_schedule

        :param dev_id: Device's unique id
        :type dev_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"device/{dev_id}/current_schedule"
        return self.get_request(path)

    def event(self, dev_id: str, starttime: int, endtime: int):
        """Retrieve events for a device entity.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicdeviceideventstarttimestarttimeendtimeendtim

        :param dev_id: Device's unique id
        :type dev_id: str

        :param starttime: Query start time milliseconds unix epoch
        :type starttime: int

        :param endtime: Query end time milliseconds unix epoch
        :type endtime: int

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"device/{dev_id}/event?startTime={starttime}&endTime={endtime}"
        return self.get_request(path)

    def forecast(self, dev_id: str, units="US"):
        """Retrieve current and predicted forecast.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicdeviceidforecastunitsunits

        :param dev_id: Device's unique id
        :type dev_id: str

        :param units: Forecast data units, one of US or METRIC, defaults to US
        :type units: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        assert units in ["US", "METRIC"], "units must be either US or METRIC"
        path = f"device/{dev_id}/forecast?units={units}"
        return self.get_request(path)

    def stop_water(self, dev_id: str):
        """Stop all watering on device.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/devicestop_water

        :param dev_id: Device's unique id
        :type dev_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"id": dev_id}
        return self.put_request("device/stop_water", payload)

    def rain_delay(self, dev_id: str, duration: int):
        """Rain delay device.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/devicestop_water

        :param dev_id: Device's unique id
        :type dev_id: str

        :param duration: Duration in seconds (Range is 0 - 604800 (7 days) )
        :type duration: int

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        assert 0 <= duration <= 604800, "duration must be between 0 and 604800"
        payload = {"id": dev_id, "duration": duration}
        return self.put_request("device/rain_delay", payload)

    def turn_on(self, dev_id: str):
        """Turn ON all features of the device.

        schedules, weather intelligence, water budget, etc.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicdeviceon-1

        :param dev_id: Device's unique id
        :type dev_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"id": dev_id}
        return self.put_request("device/on", payload)

    def turn_off(self, dev_id: str):
        """Turn OFF all features of the device.

        schedules, weather intelligence, water budget, etc.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicdeviceoff-1

        :param dev_id: Device's unique id
        :type dev_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"id": dev_id}
        return self.put_request("device/off", payload)

    def pause_zone_run(self, dev_id: str, duration: int):
        """Pause a zone run for device.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicdevicepause_zone_run

        :param dev_id: Device's unique id
        :type dev_id: str

        :param duration: Duration in seconds (Range is 0 - 3600 (1 hour) )
        :type duration: int

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        assert 0 <= duration <= 3600, "duration must be between 0 and 3600"
        payload = {"id": dev_id, "duration": duration}
        return self.put_request("device/pause_zone_run", payload)

    def resume_zone_run(self, dev_id: str):
        """Resume a zone run for device.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publicdeviceresume_zone_run

        :param dev_id: Device's unique id
        :type dev_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"id": dev_id}
        return self.put_request("device/resume_zone_run", payload)
