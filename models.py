class Status:
    """
    print(json.dumps(tba.status(), indent=4))
    {
        "android": {
            "latest_app_version": 4020399,
            "min_app_version": -1
        },
        "backup": {},
        "contbuild_enabled": true,
        "current_season": 2017,
        "down_events": [],
        "ios": {
            "latest_app_version": -1,
            "min_app_version": -1
        },
        "is_datafeed_down": false,
        "max_season": 2018
    }
    """

    def __init__(self, json):
        # App status
        self.android = MobileApp(json.get('android'))
        self.ios = MobileApp(json.get('ios'))

        # Server Status
        self.feed_down = json.get('is_datafeed_down')
        self.continuous_build_enabled = json.get('contbuild_enabled')

        self.backup = json.get('backup')
        self.down_events = json.get('down_events')

        # Season information
        self.current_season = json.get('current_season')
        self.max_season = json.get('max_season')


class Rankings:
    pass


class Team:
    """
    print(json.dumps(tba.team(5549), indent=4))
    {
        "address": null,
        "city": "Falls Church",
        "country": "USA",
        "gmaps_place_id": null,
        "gmaps_url": null,
        "home_championship": {
            "2017": "St. Louis",
            "2018": "Detroit"
        },
        "key": "frc5549",
        "lat": null,
        "lng": null,
        "location_name": null,
        "motto": null,
        "name": "Nvidia/Harris Teeter/General Dynamics/Jamie Hyneman&Marshall High",
        "nickname": "Gryphon Robotics",
        "postal_code": "22043",
        "rookie_year": 2015,
        "state_prov": "Virginia",
        "team_number": 5549,
        "website": "https://www.frc5549.org/"
    }
    """

    def __init__(self, json):
        # Team information
        self.team_number = json.get('team_number')
        self.key = json.get('key')

        self.name = json.get('name')
        self.nickname = json.get('nickname')
        self.rookie_year = json.get('rookie_year')

        # Location information
        self.address = json.get('address')
        self.city = json.get('city')
        self.state_or_providence = json.get('state_prov')
        self.postal_code = json.get('postal_code')
        self.country = json.get('country')

        self.latitude = json.get('lat')
        self.longitude = json.get('lng')
        self.location_name = json.get('location_name')

        self.google_maps_place_id = json.get('gmaps_place_id')
        self.google_maps_url = json.get('gmaps_url')

        # Errata
        self.home_championship = HomeChampionship(json.get('home_championship'))
        self.motto = json.get('motto')
        self.website = json.get('website')


class Event:
    """
    print(json.dumps(tba.event('2017vahay'), indent=4))
    {
        "address": "15000 Graduation Dr, Haymarket, VA 20169, USA",
        "city": "Haymarket",
        "country": "USA",
        "district": {
            "abbreviation": "chs",
            "display_name": "Chesapeake",
            "key": "2017chs",
            "year": 2017
        },
        "division_keys": [],
        "end_date": "2017-03-05",
        "event_code": "vahay",
        "event_type": 1,
        "event_type_string": "District",
        "first_event_id": "22495",Ri
        "gmaps_place_id": "ChIJMbVQGL5otokRYPVVdE1euFQ",
        "gmaps_url": "https://maps.google.com/?cid=6104732981657990496",
        "key": "2017vahay",
        "lat": 38.8453326,
        "lng": -77.6298068,
        "location_name": "Battlefield High School",
        "name": "CHS District - Northern Virginia Event sponsored by Bechtel",
        "parent_event_key": null,
        "playoff_type": null,
        "playoff_type_string": null,
        "postal_code": "20169",
        "short_name": "Northern Virginia",
        "start_date": "2017-03-03",
        "state_prov": "VA",
        "timezone": "America/New_York",
        "webcasts": [
            {
                "channel": "17752602",
                "file": "7077017",
                "type": "livestream"
            }
        ],
        "website": "http://www.firstchesapeake.org",
        "week": 0,
        "year": 2017
    }
    """

    def __init__(self, json):
        # Event information
        self.key = json.get('key')
        self.name = json.get('name')
        self.short_name = json.get('short_name')

        self.event_code = json.get('event_code')
        self.event_type = json.get('event_type')
        self.event_type_string = json.get('event_type_string')

        self.first_event_code = json.get('first_event_code')
        self.first_event_id = json.get('first_event_id')

        self.district = District(json.get('district'))
        self.division_keys = json.get('division_keys')
        self.parent_event_key = json.get('parent_event_key')

        self.playoff_type = json.get('playoff_type')
        self.playoff_type_string = json.get('playoff_type_string')

        # Time information
        self.week = json.get('week')
        self.year = json.get('year')

        self.start_date = json.get('start_date')
        self.end_date = json.get('end_date')

        self.timezone = json.get('timezone')

        # Location information
        self.address = json.get('address')
        self.city = json.get('city')
        self.state_or_providence = json.get('state_prov')
        self.postal_code = json.get('postal_code')
        self.country = json.get('country')

        self.latitude = json.get('lat')
        self.longitude = json.get('lng')
        self.location_name = json.get('location_name')

        self.google_maps_place_id = json.get('gmaps_place_id')
        self.google_maps_url = json.get('gmaps_url')

        # Errata
        self.webcasts = [Webcast(raw) for raw in json.get('webcasts')]
        self.website = json.get('website')
        

class Award:
    pass


class Media:
    pass


class Robot:
    pass


class District:
    def __init__(self, json):
        self.abbreviation = json.get('abbreviation')
        self.display_name = json.get('display_name')
        self.key = json.get('key')
        self.year = json.get('year')


class Profile:
    pass


class Alliance:
    pass


class Insights:
    pass


class OPRs:
    pass


class Predictions:
    pass


class Match:
    pass


class DistrictRanking:
    pass


class MobileApp:
    def __init__(self, json):
        self.latest_app_version = json.get('latest_app_version')
        self.min_app_version = json.get('min_app_version')


class HomeChampionship:
    def __init__(self, json):
        self.cmp2017 = json.get('2017')
        self.cmp2018 = json.get('2018')


class Webcast:
    def __init__(self, json):
        self.channel = json.get('channel')
        self.file = json.get('file')
        self.type = json.get('type')
