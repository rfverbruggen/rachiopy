"""Valve Service."""

from rachiopy.rachioobject import RachioObject


class Valve(RachioObject):
    """Valve class for smart hose timer."""

    def get_base_station(self, base_id: str):
        """Retreive the information for a specific base station.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/valveservice_getbasestation

        :param base_id: Base station's unique id
        :type user_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"valve/getBaseStation/{base_id}"
        return self.valve_get_request(path)

    def get_valve(self, valve_id: str):
        """Retrieve the information for a specific smart valve.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/valveservice_getvalve

        :param valve_id: Valve's unique id
        :type user_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"valve/getValve/{valve_id}"
        return self.valve_get_request(path)

    def list_base_stations(self, user_id: str):
        """Retrieve all base stations for a given user ID.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/valveservice_listbasestations

        :param user_id: Person's unique id
        :type user_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"valve/listBaseStations/{user_id}"
        return self.valve_get_request(path)

    def list_valves(self, base_id: str):
        """Retreive all valves on a given base station.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/valveservice_listvalves

        :param base_id: Base station's unique id
        :type user_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"valve/listValves/{base_id}"
        return self.valve_get_request(path)

    def set_default_runtime(self, valve_id: str, duration: int):
        """Set the runtime for a valve when the button is pressed.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/valveservice_setdefaultruntime

        :param valve_id: Valve's unique id
        :type user_id: str

        :param duration: Duration in seconds
        :type duration: int

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"valveId": valve_id, "defaultRuntimeSeconds": duration}
        return self.valve_put_request("valve/setDefaultRuntime", payload)

    def start_watering(self, valve_id: str, duration: int):
        """Start a valve.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/valveservice_startwatering

        :param valve_id: Valve's unique id
        :type user_id: str

        :param duration: Duration in seconds
        :type duration: int

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        assert 0 <= duration <= 86400, "duration must be in range 0-86400"
        payload = {"valveId": valve_id, "durationSeconds": duration}
        return self.valve_put_request("valve/startWatering", payload)

    def stop_watering(self, valve_id: str):
        """Stop a valve.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/valveservice_stopwatering

        :param valve_id: Valve's unique id
        :type user_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"valveId": valve_id}
        return self.valve_put_request("valve/stopWatering", payload)
