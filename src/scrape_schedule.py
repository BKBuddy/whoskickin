from datetime import date, datetime, timedelta
import logging
import os
import schedule
import time

from twilio.rest import Client

from scrape_service import ScrapeKickoffData


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

account_sid = 'AC4489547a569bd20a6301e90d606fb3dd'
auth_token = os.environ.get('TWILIO_TOKEN')
twilio = Client(account_sid, auth_token)

def send_are_you_ready_sms():
    is_game_today, games_this_week = _check_for_games_today()
    if not is_game_today:
        return
    now = datetime.now()
    later = now + timedelta(hours=2)
    games_to_message = {eid:game for eid, game in games_this_week.items() if now < game['kickoff_datetime'] < later}
    message = twilio.messages.create(body=str(games_to_message), from_='+12169302380', to='+12168322276')
    log.info('Message info is: {}'.format(message))

def _check_for_games_today():
    scrape = ScrapeKickoffData()
    games_this_week = scrape.get_current_week_game_data()
    game_dates = _get_game_dates(games_this_week)
    is_game_today = any(game_date == date.today() for game_date in game_dates)
    log.info('Is there a game today? Schedule says: {}'.format(is_game_today))
    return is_game_today, games_this_week

def _get_game_dates(games_this_week):
    return {game['kickoff_datetime'].date() for game in games_this_week.values()}

# Create schedule for sending game time reminder sms messages
schedule.every().thursday.at('19:30').do(send_are_you_ready_sms)
schedule.every().sunday.at('12:30').do(send_are_you_ready_sms)
schedule.every().sunday.at('15:30').do(send_are_you_ready_sms)
schedule.every().monday.at('19:30').do(send_are_you_ready_sms)
# Playoffs
schedule.every().saturday.at('12:30').do(send_are_you_ready_sms)
schedule.every().saturday.at('15:30').do(send_are_you_ready_sms)

# testing scheduler
# schedule.every(5).seconds.do(send_are_you_ready_sms)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
