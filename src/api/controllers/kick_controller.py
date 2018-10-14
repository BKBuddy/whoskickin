import logging

from services.kick_service import get_current_week_eids, get_single_game_kicking_data

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def get_all_kicks():
    """
    This calls the single game feed for each game and builds a dictionary that uses a game's eid as the key. The value
    is a list containing two dictionaries - one for each team. The team dictionary contains a str of the team
    abbreviation, a boolean if the team is home, and a boolean if the team will kickoff in the second half. is_kickoff
    will be None/null if the first half kick has not been posted to nfl.com yet.

    :return: {
                eid : [
                        {
                            "team_abbr": str
                            "is_home": bool
                            "is_kicking": bool
                        },
                        {
                            "team_abbr": str
                            "is_home": bool
                            "is_kicking": bool
                        }
                    ],
                eid: [{}, {}], ...

            }
    """
    eids = get_current_week_eids()
    return {eid: get_single_game_kicking_data(eid)[eid] for eid in eids}

def get_single_game(eid):
    """
    This calls the single game feed for the eid provided and builds a dictionary that uses a game's eid as the key.
    The value is a list containing two dictionaries - one for each team. The team dictionary contains a str of the team
    abbreviation, a boolean if the team is home, and a boolean if the team will kickoff in the second half. is_kickoff
    will be None/null if the first half kick has not been posted to nfl.com yet.
    :param eid: str

    :return: {
                eid : [
                        {
                            "team_abbr": str
                            "is_home": bool
                            "is_kicking": bool
                        },
                        {
                            "team_abbr": str
                            "is_home": bool
                            "is_kicking": bool
                        }
                    ]
                }
    """
    return get_single_game_kicking_data(eid)
