"""Zone module handling /zone/ API calls."""

from decimal import Decimal

from rachiopy.rachioobject import RachioObject


class Zone(RachioObject):
    """Zone class with methods for /zone/ API calls."""

    def start(self, zone_id: str, duration: int):
        """Start a zone.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/zonestart

        :param zone_id: Zone's unique id
        :type zone_id: str

        :param duration: Duration in seconds (Range is 0 - 10800 (3 Hours) )
        :type duration: int

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        assert 0 <= duration <= 10800, "duration must be in range 0-10800"
        payload = {"id": zone_id, "duration": duration}
        return self.put_request("zone/start", payload)

    def start_multiple(self, zones):
        """Start multiple zones.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publiczonestart_multiple

        :param zones: Zone's unique id, duration, and sort order
        :type zones: Object[]

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"zones": zones}
        return self.put_request("zone/start_multiple", payload)

    def schedule(self):
        """Create an empty zone schedule."""
        return ZoneSchedule(self)

    def set_moisture_percent(self, zone_id: str, percent: Decimal):
        """Set zone moisture percent.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publiczonesetmoisturepercent

        :param zone_id: Zone's unique id
        :type zone_id: str

        :param percent: Soil moisture percent (Range is 0 - 1 )
        :type percent: Decimal

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        assert 0 <= percent <= 1, "percent must be in range 0.0-1.0"
        payload = {"id": zone_id, "percent": percent}
        return self.put_request("zone/setMoisturePercent", payload)

    def set_moisture_level(self, zone_id: str, level: Decimal):
        """Set zone moisture level.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publiczonesetmoisturelevel

        :param zone_id: Zone's unique id
        :type zone_id: str

        :param level: Soil moisture level in mm (Range is 0 - Maximum Moisture
        in mm (depth of water + (10% depth of water))
        :type level: Decimal

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"id": zone_id, "level": level}
        return self.put_request("zone/setMoistureLevel", payload)

    def get(self, zone_id: str):
        """Retrieve the information for a zone entity.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/publiczoneid

        :param zone_id: Zone's unique id
        :type zone_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"zone/{zone_id}"
        return self.get_request(path)


class ZoneSchedule:
    """Help with starting multiple zones."""

    def __init__(self, zone_api: Zone):
        """Zoneschedule class initializer."""
        self._api = zone_api
        self._zones = []

    def enqueue(self, zone_id: str, duration: int):
        """Add a zone and duration to the schedule.

        :param zone_id: Zone's unique id
        :type zone_id: str

        :param duration: Duration in seconds (Range is 0 - 10800 (3 Hours) )
        :type duration: int
        """
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
