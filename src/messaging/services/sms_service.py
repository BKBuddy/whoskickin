import json
import logging
from datetime import date, datetime, timedelta

import requests
from twilio.rest import Client

from services.config_service import ACCOUNT_SID, AUTH_TOKEN, BASE_API_URL, RECIPIENT_PHONE_NUMBERS, TWILIO_PHONE

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

twilio = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms_message():
    is_game_today, games_this_week = _check_for_games_today()
    if not is_game_today or not games_this_week:
        return
    message_body = _get_kickoff_message(games_this_week)
    if message_body is None:
        log.debug('Message body returned None, not sending sms')
        return
    message_body = '{}{}'.format('-\n\n', message_body)
    for recipient_phone_number in RECIPIENT_PHONE_NUMBERS:
        message = twilio.messages.create(
            body=message_body,
            from_=TWILIO_PHONE,
            to=recipient_phone_number)
        log.info('Message info is: {}'.format(message))

def _get_kickoff_message(games_this_week):
    message_body = None
    now = datetime.now()
    earlier = now - timedelta(hours=2)
    eids = []
    kickoff_times = []
    for eid, game in games_this_week.items():
        if earlier < datetime.strptime(game['kickoff_datetime'], '%Y-%m-%dT%H:%M:%SZ') < now:
            eids.append(eid)
            kickoff_times.append(datetime.strptime(game['kickoff_datetime'], '%Y-%m-%dT%H:%M:%SZ').strftime('%I:%M %p'))
    all_kicking_teams = [_get_data_from_api(endpoint='single_game', eid=eid) for eid in eids]
    if any(team is None for team in all_kicking_teams):
        return None
    for idx, kickoff_time in enumerate(kickoff_times):
            log.debug('kicking team dictionary / list is of type: {} and is: {}'.format(type(all_kicking_teams), all_kicking_teams))
            if [game['kicking_team'] for game in all_kicking_teams[idx].values()][0]:
                game = list(all_kicking_teams[idx].values())[0]
                receive_team = game['home_team'] if game['kicking_team'] == game['away_team'] else game['away_team']
                kicking_team = game['kicking_team']
            else:
                receive_team = None
                kicking_team = None
            message_body = 'Game Time: {}\n2nd half:\nKicking: {}\nReceiving: {}\n\n'.format(
                kickoff_time,
                kicking_team,
                receive_team
            )
    return message_body

def _check_for_games_today():
    is_game_today = None
    games_this_week = _get_data_from_api(endpoint='schedule')
    if games_this_week:
        game_dates = _get_game_dates(games_this_week)
        is_game_today = any(game_date == date.today() for game_date in game_dates)
        log.info('Is there a game today? Schedule says: {}'.format(is_game_today))
    return is_game_today, games_this_week

def _get_game_dates(games_this_week):
    return {datetime.strptime(game['kickoff_datetime'], '%Y-%m-%dT%H:%M:%SZ').date() for game in games_this_week.values()}

def _get_data_from_api(endpoint, eid=None):
    retry_counter = 0
    api_data = None
    url = '{}/{}'.format(BASE_API_URL, endpoint)
    if eid:
        url = '{}/{}'.format(url, eid)
    log.debug('url is: {}'.format(url))
    while not api_data and retry_counter < 3:
        try:
            api_data = requests.get(url).json()
        except requests.exceptions.Timeout as ex:
            retry_counter += 1
            log.error('Error reaching: {}\n{}'.format(url, ex))
        except json.decoder.JSONDecodeError:
            log.error('No data returned from url: {}'.format(url))
            return api_data
    return api_data
