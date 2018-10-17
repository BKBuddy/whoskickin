import os

ACCOUNT_SID = os.environ.get('TWILIO_SID')
AUTH_TOKEN = os.environ.get('TWILIO_TOKEN')
BASE_API_URL = os.environ.get('API_URL')
RECIPIENT_PHONE_NUMBERS = os.environ.get('RECIPIENT_PHONE_NUMBERS').split(',')
TWILIO_PHONE = os.environ.get('TWILIO_PHONE')
TEST_MODE = os.environ.get('TEST_MODE', False)
