import xml.etree.ElementTree as ET
import logging
from datetime import datetime

import requests
import json

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    scraper = ScrapeKickoffData()
    eids = scraper.get_current_week_eids()
    kicking_and_receiving_teams = [scraper.get_single_game_kicking_data(eid) for eid in eids]
    print("""
## ----------------------------------------------------------------------------------------------##
##                                                                                               ##
##                                ARE YOU READY FOR SOME FOOTBALL!!!                             ##
##                                                                                               ##
## ----------------------------------------------------------------------------------------------## 
                                                ▗
                                               ▟▜▄
                                             ▄▛█▜▛▙▖
                            ▖             ▗▄█▙█▜▛█▜█▙▄              ▗
                            ▛█▄▖▖    ▗▗▄▞█▜▙▙█▟▛▛▀▀▝▀▛██▄▄▖▖   ▖▖▄▄█▜
                            ▛▙▛█▜██▜█▛█▟▜▛█▟▜▞▘   ▚▘ ▐█▟▜▟▜████▜▜▜▟▜▙
                            █▜▜▚ ▙▜▛▙▛▙ ▛▛▙█▘  ▄▝▀   ▗▙▜▜ █▞▙█▟▜ ▛▛█▟
                            ▜▛▙  ▗▟▜█▟  ▗▟▜▞  ▚▄▀     █▚  ▗▟▜▟▄▖ ▗▟▙▙
                            ▛█▜▄▛▄▜█▟▟▄▛▄▜█  ▜▚      ▐▛█▄▙▄▜▛▛█▗▛▄▟▟▙
                            █▜▜▟▜▜█▟▙█▟▜▜▜▟  ▌      ▗▛█▙▛▜▟▛█▜▛█▀█▟▙▙
                            ▛▛▀▘ ▀▐▙▛▞▀ ▀▀█ ▞      ▄▛█▙▀▀ ▀▀▛█▀▘▘▘▀▟▙
                            █▜█  ▐▙▙█▜   █▙▘▌   ▗▄▛▙█▙▛█  ▗█▜▙█▖  ██▟
                            ▛█▙▜█▚▟▜▟█▟█▙█▟█▄▟▟▛█▙█▛▙▛▛▙▟█▚▛█▙▛▟▜▙█▟▟
                            ▛▙▀▀▝▀▀▀▘▀▝▝▝▝▘▀▀▝▘▀▘▀▝▀▘▀▀▀▘▀▀▀▘▘▀▀▀▝▝▙▙
                            █▌  ▖▖▖▖▖  ▄▄▖▄▗ ▖▖▖▖▖▖▖▖▖▖ ▖▖▖▖▖      ▙▛
                            ▙▙  ▙▜▜▟▄ ▝▟▐▞▙▜ ▞▛▜▞▛▟▜▞▛▖▐▜▚▛▟▜      ▟▜
                            █▄   ▚▙▚▚▖ ▝▚▜▞▖ ▝▐▙▜▞▝▝▞▛▌ ▚▜▟▞       ▜▛
                            ▙▌   ▐▞▛▙▚  ▛▙▜   ▚▙▚▘  ▝▘▘ ▝▙▚▜       ▜▟
                            ▛▙   ▐▞▟▞▛▖ ▛▞▙   ▐▞▛▌      ▐▞▙▙       ▜▙
                            █▌   ▐▞▙▜▞▙ ▛▟▞   ▚▜▞▄▗▞▛▖  ▗▜▞▞       ▜▟
                            ▙▌   ▐▟▞▌▛▟▖▛▟▟   ▐▚▜▞▙▜▟▖  ▝▙▜▞       ▜▙
                            ▛▌   ▐▄▚▘▞▙▚▛▟▐   ▞▛▙▘ ▘▌▖  ▐▞▙▜       ▜▟
                            █▛   ▗▙▜▘▝▞▙▜▞▙   ▐▚▙▘      ▗▜▞▌  ▐▜▚  ▜▙
                            ▙▌   ▐▞▙▘ ▐▞▙▜▞   ▐▌▙▘      ▝▙▜▞  ▐▚▛  ▜▟
                            █▌  ▙▙▜▐▚  ▛▞▙▜   ▐▞▙▘      ▐▞▙▜▞▛▙▜▞  ▜▙
                            ▙█  ▝▝▞▛▟▘ ▝▛▟▞   ▐▜▞▌     ▗▟▞▞▙▚▛▞▘▘  █▟
                            ▝▟█▖        ▀▞▟  ▞▛▟▞▖     ▝▖▀▀      ▗▟▜▞
                              ▚██▙▄▖▖        ▀▐▚▜▜▖          ▗▗▄▜█▞▘
                                 ▘▀▀██▛▙▙▄▖▖     ▘▘   ▗▄▄▟▞█▜▛▛▀▘
                                       ▘▀▘▛▛▙▄     ▄▟█▜▞▀▝▘▘
                                            ▀▀█▄ ▟▜▛▘▘
                                              ▝▜▜▛▘
                                                ▘

##           _________________                                        ___________________
##          |  KICKING TEAMS  |                                      |  RECEIVING TEAMS  |
##          |_________________|                                      |___________________|
    """, end='', flush=True)
    for kicking, receiving in kicking_and_receiving_teams:
        if kicking != 'TBD':
            print("""
##          |   {kicking}\t     |                                       |   {receiving}\t\t|
            """.format(kicking=kicking, receiving=receiving), end='', flush=True)
    if any(team == ('TBD', 'TBD') for team in kicking_and_receiving_teams):
        print("""
## ----------------------------------------------------------------------------------------------##
##                              Keep Klicking for more Kicking info!                             ##
## ----------------------------------------------------------------------------------------------##
              """)
    print("""
## ----------------------------------------------------------------------------------------------##
##                                     Brought to you by:                                        ##
##                                KICKING IT WITH KURRBERT!!!                                    ##
##                                                                                               ##
## ----------------------------------------------------------------------------------------------##
        """)


ANY_WEEK_OF_GAMES = 'http://www.nfl.com/ajax/scorestrip?season={season}&seasonType={season_type}&week={week}'
CURRENT_WEEK_OF_GAMES = 'http://www.nfl.com/liveupdate/scorestrip/ss.xml'
GAME_FEED = 'http://www.nfl.com/liveupdate/game-center/{eid}/{eid}_gtd.json'

headers = {
    'User-Agent': 'Whoskickin User Agent 1.0',
    'From': 'https://github.com/BKBuddy/whoskickin'
}

def get_single_game_kicking_data(eid):
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
    retry_counter = 0
    schedule = get_current_week_game_data()
    single_game_data = {
        eid: {
            'home_team': schedule[eid]['home_team_abbr'],
            'away_team': schedule[eid]['visitor_team_abbr'],
            'kicking_team': None
        }
    }
    nfl_live_data = None
    while not nfl_live_data and retry_counter < 2:
        try:
            nfl_live_data = requests.get(GAME_FEED.format(eid=eid), headers=headers).json()
        except requests.exceptions.Timeout as ex:
            retry_counter += 1
            log.error('Error encountered reaching {}: {}'.format(CURRENT_WEEK_OF_GAMES, ex))
        except json.decoder.JSONDecodeError:
            log.error('Game Data not available yet for {}.'.format(eid))
            return single_game_data

    try:
        kicking_team = nfl_live_data[eid]['drives']['1']['posteam']
    except KeyError:
        log.error('Kickoff data not available yet for {}.'.format(eid))
        return single_game_data
    single_game_data[eid]['kicking_team'] = kicking_team
    log.info('Data for EID: {} is: {}'.format(eid, single_game_data))
    return single_game_data

def get_current_week_eids():
    """
    Retrieves a list of eids from nfl.com that enables you to get live game data from json feed per game.
    :return: [strings of eid]
    """
    return [game.attrib['eid'] for game in _get_games_data_for_current_week()]

def get_any_week_eids(season, season_type, week):
    """
    Retrieves a list of eids from nfl.com that enables you to get historical, live or future game data from
    json feed per game.
    :return:
    :param season: YYYY, i.e, '2018'
    :param season_type: 'PRE', 'REG', or 'POST'
    :param week: 1-4 for PRE, 1-17 for REG, 18-20 & 21 for POST
    :return: [strings of eid]
    """
    url = ANY_WEEK_OF_GAMES.format(season=season, season_type=season_type, week=week)
    return [game.attrib['eid'] for game in _get_games_data_for_current_week(url=url)]

def get_current_week_game_data():
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
    games = _get_games_data_for_current_week()
    return {game.attrib['eid']: {
        'day': game.attrib['d'],
        'kickoff_datetime': _get_kickoff_datetime(game.attrib['eid'], game.attrib['t']),
        'game_status': game.attrib['q'],
        'home_team_abbr': game.attrib['h'],
        'home_team_name': game.attrib['hnn'],
        'home_score': game.attrib['hs'],
        'visitor_team_abbr': game.attrib['v'],
        'visitor_team_name': game.attrib['vnn'],
        'visitor_score': game.attrib['vs'],
        'game_type': game.attrib['gt']
    } for game in games}


def _get_games_data_for_current_week(url=None):
    retry_counter = 0
    games_this_week = None
    url = url if url else CURRENT_WEEK_OF_GAMES
    while not games_this_week and retry_counter < 2:
        try:
            games_this_week = requests.get(url=url, timeout=3, headers=headers)
        except requests.exceptions.Timeout as ex:
            retry_counter += 1
            log.error('Error encountered reaching {}: {}'.format(url, ex))
    return ET.fromstring(games_this_week.text)[0]


def _get_kickoff_datetime(eid, time):
    hour, minute = time.split(':')
    if len(hour) < 2:
        hour = '0{}'.format(hour)
    game_time = '{} {}:{}PM'.format(eid[:8], hour, minute)
    return datetime.strptime(game_time, '%Y%m%d %I:%M%p')

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
    return get_single_game_kicking_data(eid)


if __name__ == '__main__':
    main()
