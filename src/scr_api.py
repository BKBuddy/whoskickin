from flask import Flask
from flask_restful import Resource, Api

from scrape import ScrapeKickoffData

app = Flask(__name__)
api = Api(app)

class KickingIt(Resource):
    def get(self):
        scrape = ScrapeKickoffData()
        eids = scrape.get_current_week_eids()
        kicking_teams, receiving_teams = zip(*[scrape.get_single_game_kicking_data(eid) for eid in eids])
        return {
            'kicking_teams': kicking_teams,
            'receiving_teams': receiving_teams
        }

class Schedule(Resource):
    def get(self):
        scrape = ScrapeKickoffData()
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


api.add_resource(KickingIt, '/')
api.add_resource(Schedule, '/schedule')

if __name__ == '__main__':
    app.run(debug=True)