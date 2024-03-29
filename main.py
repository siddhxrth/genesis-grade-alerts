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
chromeOptions.add_argument("--window-size=1920,1080")
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument('--allow-running-insecure-content')
chromeOptions.add_argument(f'user-agent={userAgent}')

driver = webdriver.Chrome('./chromedriver', options=chromeOptions)

previousGrades = {}

functions.login(driver)
functions.getInitialGrades(driver, settings.classes, previousGrades)
functions.logout(driver)

def run():
  functions.login(driver)
  functions.checkAndUpdateGrades(driver, previousGrades)
  functions.logout(driver)

while True:
  run()
  time.sleep(settings.REFRESH_INTERVAL * 60)

          