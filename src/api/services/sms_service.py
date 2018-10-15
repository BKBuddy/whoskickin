from datetime import date, datetime, timedelta
import logging
import os
import schedule
import time

from twilio.rest import Client

from controllers.kick_controller import get_single_game
from controllers.schedule_controller import get_current_week_schedule

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_TOKEN')
twilio = Client(account_sid, auth_token)
twilio_phone = '+12169302380'
recipient_phone_numbers = ['+12168322276']

def send_sms_message():
    is_game_today, games_this_week = _check_for_games_today()
    if not is_game_today:
        return
    message_body = _get_kickoff_message(games_this_week)

    for recipient_phone_number in recipient_phone_numbers:
        message = twilio.messages.create(
            body=message_body,
            from_=twilio_phone,
            to=recipient_phone_number)
        log.info('Message info is: {}'.format(message))

def _get_kickoff_message(games_this_week):
    now = datetime.now()
    earlier = now - timedelta(hours=2)
    eids = []
    kickoff_times = []
    for eid, game in games_this_week.items():
        if earlier < game['kickoff_datetime'] < now:
            eids.append(eid)
            kickoff_times.append(game['kickoff_datetime'].strftime('%I:%M %p'))
    all_kicking_teams = [get_single_game(eid)[eid] for eid in eids]

    message_body = '-\n\n'
    for idx, kickoff_time in enumerate(kickoff_times):
            if all_kicking_teams[idx]['kicking_team']:
                receive_team = all_kicking_teams[idx]['home_team'] if all_kicking_teams[idx]['kicking_team'] == \
                                                                      all_kicking_teams[idx]['away_team'] \
                                                                    else all_kicking_teams[idx]['away_team']
            else:
                receive_team = None
            message_body = '{}Game Time: {}\n2nd half:\nKicking: {}\nReceiving: {}\n\n'.format(
                message_body,
                kickoff_time,
                all_kicking_teams[idx]['kicking_team'],
                receive_team
            )
    return message_body

def _check_for_games_today():
    games_this_week = get_current_week_schedule()
    game_dates = _get_game_dates(games_this_week)
    is_game_today = any(game_date == date.today() for game_date in game_dates)
    log.info('Is there a game today? Schedule says: {}'.format(is_game_today))
    return is_game_today, games_this_week

def _get_game_dates(games_this_week):
    return {game['kickoff_datetime'].date() for game in games_this_week.values()}

# Create schedule for sending kickoff sms messages
schedule.every().thursday.at('21:00').do(send_sms_message)
schedule.every().sunday.at('13:15').do(send_sms_message)
schedule.every().sunday.at('16:40').do(send_sms_message)
schedule.every().sunday.at('20:35').do(send_sms_message)
schedule.every().monday.at('20:30').do(send_sms_message)
# Playoffs
schedule.every().saturday.at('13:15').do(send_sms_message)
schedule.every().saturday.at('16:40').do(send_sms_message)

# testing scheduler - Line below should always be commented out in production
schedule.every(5).seconds.do(send_sms_message)

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
