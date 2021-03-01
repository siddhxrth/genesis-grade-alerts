from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from twilio.rest import Client

import time
import smtplib


import settings

def login(driver):
    email = settings.PARENT_ACCESS_EMAIL
    password = settings.PARENT_ACCESS_PASSWORD

    driver.get("https://parents.ebnet.org/genesis/sis/view?gohome=true")

    # find login fields

    parent_access_email = driver.find_element(By.XPATH, '//*[@id="j_username"]')
    parent_access_password  = driver.find_element(By.XPATH, '//*[@id="j_password"]')

    parent_access_email.send_keys(email)
    parent_access_password.send_keys(password)

    parent_access_password.send_keys(Keys.ENTER)

    # switch siblings
    driver.get("https://parents.ebnet.org/genesis/parents?tab1=studentdata&tab2=gradebook&tab3=weeklysummary&studentid=" + settings.STUDENT_ID + "&action=form")

    # wait for page to load before finding elements
    time.sleep(2)

def getInitialGrades(driver, classes):

  with open("grades.csv", 'w') as f:

    for subject in settings.classes:
      intialGrade = driver.find_element(By.XPATH, settings.classes[subject]).text

      f.write(subject + "," + intialGrade + "\n")


def sendNotification(method, gradeChangedMessage):

  if(method.lower() == "sms"):
    try:

      client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

      message = client.messages.create(
                to= settings.DESTINATION_PHONE_NUMBER, 
                from_= settings.TWILIO_PHONE_NUMBER,
                body=gradeChangedMessage)

      print(gradeChangedMessage + " sent to " + settings.DESTINATION_PHONE_NUMBER)

    except Exception as e:
      print(e)

  elif (method.lower() == "email"):
    try:

      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      server.login(settings.GMAIL_ACCOUNT_EMAIL, settings.GMAIL_ACCOUNT_PASSWORD)
      server.sendmail(settings.GMAIL_ACCOUNT_EMAIL, settings.PHONE_NUMBER_EMAIL, gradeChangedMessage)
      server.close()

      print(gradeChangedMessage + " sent to " + settings.PHONE_NUMBER_EMAIL)

    except Exception as e:
      print(e)


def getPreviousGrade(index):
    try:
        with open("grades.csv", 'r', newline='') as f:
            lines = f.readlines()
            classLine = lines[index].rstrip("\n").split(',')
            f.close()
            return(classLine[1])
    except:
            return 0.00

def writeNewGrade(index, className, updatedGrade):
    previousGrades = open("grades.csv").read().split("\n")
    
    previousGrades[index] = className + "," + updatedGrade

    with open("grades.csv", 'w') as f:
        f.truncate(0)
        for grade in previousGrades:
          if(grade != ''):
            f.write(grade + "\n")

def checkAndUpdateGrades(driver):
    index = 0;

    for subject in settings.classes:

        previousGrade = getPreviousGrade(index)

        newGrade = driver.find_element(By.XPATH, settings.classes[subject]).text

        # if grade changed
        if(previousGrade != newGrade):

          sendNotification(settings.NOTIFICATION_METHOD, subject + " grade changed from " + str(previousGrade) + " to " + str(newGrade))
          writeNewGrade(index, CLASS, newGrade)

        index = index + 1
