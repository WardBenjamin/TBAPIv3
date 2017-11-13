from requests import get

from models import Team, Event


class TBA:
    """
    Main library class.
    Contains methods for interacting with The Blue Alliance API v3.
    """

    URL_PRE = 'https://www.thebluealliance.com/api/v3/'
    auth_key = ''

    def __init__(self, auth_key):
        """
        Store auth key so we can reuse it as many times as we make a request.
        :param auth_key: Your application authorization key, obtainable at https://www.thebluealliance.com/account.
        """
        self.auth_key = auth_key

    def _get(self, url):
        """
        Helper method: GET data from given URL on TBA's API.
        :param url: URL string to get data from.
        :return: Requested data in JSON format.
        """
        return get(self.URL_PRE + url, headers={'X-TBA-Auth-Key': self.auth_key}).json()

    @staticmethod
    def team_key(identifier):
        """
        Take raw team number or string key and return string key.
        Used by all team-related methods to support either an integer team number or team key being passed.
        (We recommend passing an integer, just because it's cleaner. But whatever works.)
        :param identifier: int team number or str 'frc####'
        :return: string team key in format 'frc####'
        """
        return identifier if type(identifier) == str else 'frc%s' % identifier

    def status(self):
        """
        Get TBA API status information.
        :return: Data on current status of the TBA API as Status object.
        """
        return self._get('status') # TODO: Status object

    def team(self, team, simple=False):
        """
        Get data on a single specified team.
        :param simple: GET simpler data. Use if you only need basic data about the team.
        :return: Team object with data on specified team.
        """
        if simple:
            return Team(self._get('team/%s/simple' % self.team_key(team)))
        else:
            return Team(self._get('team/%s' % self.team_key(team)))

    def event(self, event, simple=False):
        """
        Get basic information about an event.
        More specific data (typically obtained with the detail_type URL parameter) can be obtained with event_alliances(), event_district_points(), event_insights(), event_oprs(), event_predictions(), and event_rankings().
        :param event: Key of event for which you desire data.
        :param simple: Get simpler data about event. Use this if you don't need the extra information provided by a standard request.
        :return: A single Event object.
        """
        if simple:
            return Event(self._get('event/%s/simple' % event))
        else:
            return Event(self._get('event/%s' % event))
