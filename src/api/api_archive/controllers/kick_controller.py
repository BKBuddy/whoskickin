import logging

from api_archive.services.kick_service import get_current_week_eids, get_single_game_kicking_data

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def get_all_kicks():
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
    return {eid: get_single_game_kicking_data(eid)[eid] for eid in eids}

def get_single_game(eid):
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
    return get_single_game_kicking_data(eid)
