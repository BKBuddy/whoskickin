import logging
import time

import schedule

from services.config_service import TEST_MODE
from services.sms_service import send_sms_message

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# Create schedule for sending kickoff sms messages
schedule.every().thursday.at('20:40').do(send_sms_message)
schedule.every().sunday.at('13:15').do(send_sms_message)
schedule.every().sunday.at('16:40').do(send_sms_message)
schedule.every().sunday.at('20:35').do(send_sms_message)
schedule.every().monday.at('20:30').do(send_sms_message)
# Playoffs
schedule.every().saturday.at('13:15').do(send_sms_message)
schedule.every().saturday.at('16:40').do(send_sms_message)

# testing scheduler - Will run every 5 seconds if TEST_MODE is true
if TEST_MODE:
    schedule.every(5).seconds.do(send_sms_message)

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()