import logging

from api_archive.services.kick_service import get_current_week_game_data

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def get_current_week_schedule():
    """
        Retrieves metadata about this week's games and returns a dictionary of dictionaries for each game.
        :return: {
                    'eid': {
                        'day': str (day of week abbreviation)
                        'kickoff_datetime': datetime of kickoff - no timezone - eastern is what nfl.com uses,
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
    return get_current_week_game_data()
