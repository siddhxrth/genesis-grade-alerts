# Siddharth Lohani
# 2/25/2021

# selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# scheduling tasks
import schedule
import time

# import other scripts in directory
import settings
import functions

userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

# setting up chrome driver
chromeOptions = Options()
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--disable-dev-shm-usage')
chromeOptions.add_argument('--headless')
chromeOptions.add_argument("--window-size=1920,1080")
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument('--allow-running-insecure-content')
chromeOptions.add_argument(f'user-agent={userAgent}')

driver = webdriver.Chrome('chromedriver', options=chromeOptions)


# initial setup
functions.login(driver)
functions.getInitialGrades(driver, settings.classes)


def main():
  functions.login(driver)
  functions.checkAndUpdateGrades(driver)

schedule.every(int(settings.REFRESH_INTERVAL)).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)


          