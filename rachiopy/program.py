"""Program module for the smart hose timer."""

from rachiopy.rachioobject import RachioObject


class Program(RachioObject):
    """Program class for the smart hose timer."""

    def list_programs(self, valve_id: str):
        """Retreive the list of programs (schedules) for a valve.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/programservice_listprograms

        :param valve_id: Valve's unique id
        :type valve_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        path = f"program/listPrograms/{valve_id}"
        return self.valve_get_request(path)

    def get_program(self, program_id: str):
        """Retreive the information for a specific program.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/programservice_getprogram

        :param program_id: Program's unique id
        :type program_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        path = f"program/getProgram/{program_id}"
        return self.valve_get_request(path)

    def create_skip_overrides(self, program_id: str, timestamp: str):
        """Create manual skips for the specific program run time.
        You can retrieve the runtimes from SummaryService.getValveDayViews

        For more info of the content in the response see:
        https://rachio.readme.io/docs/programservice_createskipoverrides

        :param program_id: Program's unique id
        :type program_id: str

        :param timestamp: Timestamp of the run to skip
        :type timestamp: timestamp

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"programId": program_id, "timestamp": timestamp}
        return self.valve_post_request("program/createSkipOverrides", payload)

    def delete_skip_overrides(self, program_id: str, timestamp: str):
        """Cancel program skips for the specified program run time.
        You can retrieve upcoming skips from SummaryService.getValveDayViews

        For more info of the content in the response see:
        https://rachio.readme.io/docs/programservice_deleteskipoverrides

        :param program_id: Program's unique id
        :type program_id: str

        :param timestamp: Timestamp of the run skip to delete
        :type timestamp: timestamp

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """
        payload = {"programId": program_id, "timestamp": timestamp}
        return self.valve_post_request("program/deleteSkipOverrides", payload)
