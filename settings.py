import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# credentials for parent access
PARENT_ACCESS_EMAIL  = os.environ.get("PARENT_ACCESS_EMAIL")
PARENT_ACCESS_PASSWORD  = os.environ.get("PARENT_ACCESS_PASSWORD")

# twilio api keys
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# gmail credentials
GMAIL_ACCOUNT_EMAIL = os.environ.get("GMAIL_ACCOUNT_EMAIL")
GMAIL_ACCOUNT_PASSWORD = os.environ.get("GMAIL_ACCOUNT_PASSWORD")

# phone numbers
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
DESTINATION_PHONE_NUMBER = os.environ.get("DESTINATION_PHONE_NUMBER")

# phone number to email
PHONE_NUMBER_EMAIL = os.environ.get("PHONE_NUMBER_EMAIL")

NOTIFICATION_METHOD = os.environ.get("NOTIFICATION_METHOD")

REFRESH_INTERVAL = os.environ.get("REFRESH_INTERVAL")

STUDENT_ID = os.environ.get("STUDENT_ID")

classes = {

    "CLASS ONE": "XPATH ONE",

    "CLASS TWO": "XPATH TWO",

    "CLASS THREE": "XPATH THREE",

    "CLASS FOUR": "XPATH FOUR",

    "CLASS FIVE": "XPATH FIVE",

    "CLASS SIX": "XPATH SIX",

    "CLASS SEVEN": "XPATH SEVEN"
    
    }

