import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())





###
### YOU HAVE TO FILL OUT ALL OF THESE FIELDS FOR THE PROGRAM TO WORK
###

# credentials for parent access
PARENT_ACCESS_EMAIL  = ""
PARENT_ACCESS_PASSWORD  = ""

# either push, sms, or email
NOTIFICATION_METHOD = "push"

# in minutess
REFRESH_INTERVAL = 1

# school student id
STUDENT_ID = ""

# replace this with your class names and XPATHs to them
classes = {

    "English 10H": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[1]/div",

    "AP US History": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr/td[1]/div",

    "Chem H": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td[3]/table/tbody/tr/td[1]/div",

    "Pre-Calc H": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[6]/td[3]/table/tbody/tr/td[1]/div",

    "Spanish V H": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[7]/td[3]/table/tbody/tr/td[1]/div",

    "AP CS A": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[8]/td[3]/table/tbody/tr/td[1]/div",

    "Physical Education": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[10]/td[3]/table/tbody/tr/td[1]/div"
    
    }





###
### ONLY FILL OUT IF USING TWILIO FOR NOTIFICATIONS
###

# twilio api keys
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""

# phone numbers
TWILIO_PHONE_NUMBER = ""
DESTINATION_PHONE_NUMBER = ""





###
### ONLY FILL OUT IF USING EMAIL FOR NOTIFICATIONS
###

# gmail credentials
GMAIL_ACCOUNT_EMAIL = ""
GMAIL_ACCOUNT_PASSWORD = ""

# email to send notifications to
DESTINATION_EMAIL = ""






###
### ONLY FILL OUT IF USING SPONTIT FOR NOTIFICATIONS (RECOMMENDED)
###

SPONTIT_USERNAME = ""
SPONTIT_SECCRET_KEY = ""