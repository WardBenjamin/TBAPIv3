"""
MIT License

Copyright (c) 2017 Benjamin Ward

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class Status:
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
    def __init__(self, json):
        self.extra_stats_info = json.get('extra_stats_info')
        self.rankings = json.get('rankings')
        self.sort_order_info = json.get('sort_order_info')


class Team:
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
        self.home_championship = None if json.get('home_championship') is None else HomeChampionship(json.get('home_championship'))
        self.motto = json.get('motto')
        self.website = json.get('website')


class Event:
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

        self.district = None if json.get('district') is None else District(json.get('district'))
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
        self.webcasts = [WebCast(raw) for raw in json.get('webcasts')]
        self.website = json.get('website')


class Award:
    def __init__(self, json):
        self.award_type = json.get('award_type')
        self.event_key = json.get('event_key')
        self.name = json.get('name')
        self.recipient_list = json.get('recipient_list')
        self.year = json.get('year')


class Media:
    def __init__(self, json):
        self.key = json.get('key')
        self.type = json.get('type')


class Robot:
    def __init__(self, json):
        self.key = json.get('key')
        self.robot_name = json.get('robot_name')
        self.team_key = json.get('team_key')
        self.year = json.get('year')


class District:
    def __init__(self, json):
        self.abbreviation = json.get('abbreviation')
        self.display_name = json.get('display_name')
        self.key = json.get('key')
        self.year = json.get('year')


class Profile:
    def __init__(self, json):
        self.details = json.get('details')
        self.foreign_key = json.get('foreign_key')
        self.preferred = json.get('preferred')
        self.type = json.get('type')


class Alliance:
    def __init__(self, json):
        self.disqualified_team_keys = json.get('dq_team_keys')
        self.score = json.get('score')
        self.surrogate_team_keys = json.get('surrogate_team_keys')
        self.team_keys = json.get('team_keys')


class Insights:
    def __init__(self, json, year):
        self.year = year

        # If we don't have a specific detail class, just return the raw JSON.
        if year == 2017:
            self.qualifier = InsightsDetail2017(json.get('qual'))
            self.playoff = InsightsDetail2017(json.get('playoff'))
        else:
            self.qualifier = json.get('qual')
            self.playoff = json.get('playoff')


class InsightsDetail2017:
    def __init__(self, json):
        self.average_foul_score = json.get('average_foul_score')
        self.average_fuel_points = json.get('average_fuel_points')
        self.average_fuel_points_auto = json.get('average_fuel_points_auto')
        self.average_fuel_points_teleop = json.get('average_fuel_points_teleop')
        self.average_high_goals = json.get('average_high_goals')
        self.average_high_goals_auto = json.get('average_high_goals_auto')
        self.average_high_goals_teleop = json.get('average_high_goals_teleop')
        self.average_low_goals = json.get('average_low_goals')
        self.average_low_goals_auto = json.get('average_low_goals_auto')
        self.average_low_goals_teleop = json.get('average_low_goals_teleop')
        self.average_mobility_points_auto = json.get('average_mobility_points_auto')
        self.average_points_auto = json.get('average_points_auto')
        self.average_points_teleop = json.get('average_points_teleop')
        self.average_rotor_points = json.get('average_rotor_points')
        self.average_rotor_points_auto = json.get('average_rotor_points_auto')
        self.average_rotor_points_teleop = json.get('average_rotor_points_teleop')
        self.average_score = json.get('average_score')
        self.average_takeoff_points_teleop = json.get('average_takeoff_points_teleop')
        self.average_win_margin = json.get('average_win_margin')
        self.average_win_score = json.get('average_win_score')
        self.high_kpa = json.get('high_kpa')
        self.high_score = json.get('high_score')
        self.kpa_achieved = json.get('kpa_achieved')
        self.mobility_counts = json.get('mobility_counts')
        self.rotor_1_engaged = json.get('rotor_1_engaged')
        self.rotor_1_engaged_auto = json.get('rotor_1_engaged_auto')
        self.rotor_2_engaged = json.get('rotor_2_engaged')
        self.rotor_2_engaged_auto = json.get('rotor_2_engaged_auto')
        self.rotor_3_engaged = json.get('rotor_3_engaged')
        self.rotor_4_engaged = json.get('rotor_4_engaged')
        self.takeoff_counts = json.get('takeoff_counts')
        self.unicorn_matches = json.get('unicorn_matches')


class OPRs:
    def __init__(self, json):
        self.CCWMs = json.get('ccwms')
        self.DPRs = json.get('dprs')
        self.OPRs = json.get('oprs')


class Predictions:
    def __init__(self, json):
        self.match_prediction_stats = json.get('match_prediction_stats')
        self.match_predictions = json.get('match_predictions')
        self.ranking_prediction_stats = json.get('ranking_prediction_stats')
        self.ranking_predictions = json.get('ranking_predictions')
        self.stat_mean_vars = json.get('stat_mean_vars')


class Match:
    def __init__(self, json):
        self.key = json.get('key')
        self.event_key = json.get('event_key')
        self.match_number = json.get('match_number')

        self.comp_level = json.get('comp_level')
        self.set_number = json.get('set_number')

        self.score_breakdown = json.get('score_breakdown')

        self.red_alliance = Alliance(json.get('alliances').get('red'))
        self.blue_alliance = Alliance(json.get('alliances').get('blue'))
        self.winning_alliance = json.get('winning_alliance')

        self.time = json.get('time')
        self.actual_time = json.get('actual_time')
        self.predicted_time = json.get('predicted_time')
        self.post_result_time = json.get('post_result_time')

        self.videos = [Media(raw) for raw in json.get('videos')]


class DistrictPoints:
    def __init__(self, json):
        self.points = json.get('points')
        self.tiebreakers = json.get('tiebreakers')


class DistrictRanking:
    def __init__(self, json):
        self.event_points = json.get('event_points')
        self.point_total = json.get('point_total')
        self.rank = json.get('rank')
        self.rookie_bonus = json.get('rookie_bonus')
        self.team_key = json.get('team_key')


class MobileApp:
    def __init__(self, json):
        self.latest_app_version = json.get('latest_app_version')
        self.min_app_version = json.get('min_app_version')


class HomeChampionship:
    def __init__(self, json):
        self.cmp2017 = json.get('2017')
        self.cmp2018 = json.get('2018')


class WebCast:
    def __init__(self, json):
        self.channel = json.get('channel')
        self.file = json.get('file')
        self.type = json.get('type')
