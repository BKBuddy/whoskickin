import logging
import json

from flask import Flask
from flask_cors import CORS

from services.kicking_service import get_single_game_kicking_data, get_current_week_eids, get_current_week_game_data

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/all_kicks', methods=['GET'])
def all_kicks():
    """
    This calls the single game feed for all games this week and builds a dictionary of dictionaries that uses a game's
    eid as the key. The game dictionary contains home team abbreviation, away team and the team that will kickoff in the
    second half. If the kickoff has yet to occur the kicking team is None.

    :return: {
                "eid" :
                        {
                            "home_team": str
                            "away_team": str
                            "kicking_team": str / None
                        },
                "eid" :
                        {
                            "home_team": str
                            "away_team": str
                            "kicking_team": str / None
                        }...
                }
        """
    eids = get_current_week_eids()
    all_kicks_data = {eid: get_single_game_kicking_data(eid)[eid] for eid in eids}
    return json.dumps(all_kicks_data)


@app.route('/single_game/<eid>', methods=['GET'])
def single_game(eid):
    """
    This calls the single game feed for the eid provided and builds a dictionary that uses a game's eid as the key. The
    game dictionary contains home team abbreviation, away team and the team that will kickoff in the second half. If the
    kickoff has yet to occur the kicking team is None.
    :param eid: str

    :return: {
                "eid" :
                        {
                            "home_team": str
                            "away_team": str
                            "kicking_team": str / None
                        }
                }
    """
    return json.dumps(get_single_game_kicking_data(eid))


@app.route('/schedule', methods=['GET'])
def get_current_week_schedule():
    """
        Retrieves metadata about this week's games and returns a dictionary of dictionaries for each game.
        :return: {
                    'eid': {
                        'day': str (day of week abbreviation)
                        'kickoff_datetime': string datetime
                        'game_status': F, P, or SOMETHING ELSE - final, pending or ... what is in progress?,
                        'home_team_abbr': str,
                        'home_team_name': str,
                        'home_score': int
                        'visitor_team_abbr': str,
                        'visitor_team_name': str,
                        'visitor_score': int,
                        'game_type': str
                    }...
                }
        """
    schedule = get_current_week_game_data()
    for eid, game in schedule.items():
        game['kickoff_datetime'] = game['kickoff_datetime'].strftime('%Y-%m-%d %H:%M:%S')
    return json.dumps(schedule)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
