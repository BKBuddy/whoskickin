from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_caching import Cache

from scrape_service import ScrapeKickoffData

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
api = Api(app)
scrape = ScrapeKickoffData()


class AllKicks(Resource):
    @cache.cached(30, key_prefix='all_kicks')
    def get(self):
        """
        This calls the single game feed for each game and builds a dictionary containing lists of kicking and receiving
        teams. If a game has not started, the team abbr returned is "TBD".
        May need to optimize by only looking up games that are currently being played or have played in the past.
        being played.
        :return: {
                    'kicking_teams': ["team_abbr", ...],
                    'receiving_teams': ["team_abbr", ...]
                }
        """
        eids = scrape.get_current_week_eids()
        kicking_teams, receiving_teams = zip(*[scrape.get_single_game_kicking_data(eid) for eid in eids])
        return {
            'kicking_teams': kicking_teams,
            'receiving_teams': receiving_teams
        }

class AllKicksForWeek(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('season')
    parser.add_argument('season_type')
    parser.add_argument('week')

    def get(self):
        args = self.parser.parse_args()
        eids = scrape.get_any_week_eids(args['season'], args['season_type'], args['week'])
        kicking_teams, receiving_teams = zip(*[scrape.get_single_game_kicking_data(eid) for eid in eids])
        return {
            'kicking_teams': kicking_teams,
            'receiving_teams': receiving_teams
        }

class SingleGameKick(Resource):
    def get(self, eid):
        kicking_team, receiving_team = scrape.get_single_game_kicking_data(eid)
        return {
            'kicking_team': kicking_team,
            'receiving_team': receiving_team
        }

class Schedule(Resource):
    def get(self):
        schedule = Schedule._stringify_datetime(scrape.get_current_week_game_data())
        return schedule

    @staticmethod
    def _stringify_datetime(schedule):
        """
        JSON is dumb so you have to turn a datetime object into a string.
        :param schedule:
        :return: schedule
        """
        eids = schedule.keys()
        for eid in eids:
            schedule[eid]['kickoff_datetime'] = schedule[eid]['kickoff_datetime'].strftime('%Y-%m-%d %I:%M %p')
        return schedule


api.add_resource(AllKicks, '/')
api.add_resource(Schedule, '/schedule')
api.add_resource(SingleGameKick, '/<string:eid>')
api.add_resource(AllKicksForWeek, '/search_by_week')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)