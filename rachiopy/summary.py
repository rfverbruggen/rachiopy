"""Smart Hose Timer scheudle summary calls."""

from rachiopy.rachioobject import RachioObject


class SummaryServce(RachioObject):
    """Scheudle summary class."""

    def get_valve_day_views(self, base_id: str, start, end):
        """List historical and upcoming valve runs and skips.

        For more info of the content in the response see:
        https://rachio.readme.io/docs/summaryservice_getvalvedayviews

        :param base_id: Base's unique id
        :type dev_id: str

        :param start: Start date
        :type start: Object[]

        :param end: End date
        :type end: Object[]

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body.
        :rtype: tuple
        """
        payload = {
            "resourceId": {"baseStationId": base_id},
            "start": start,
            "end": end,
        }
        return self.valve_post_request("summary/getValveDayViews", payload)
