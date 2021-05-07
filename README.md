# Genesis Grade Alerts
#### A simple Python application which notifies users when their grades are updated in the Genesis Parent Portal via SMS, either through Gmail's SMTP server or via Twilio's SMS API, or through the Spontit App (recommended).

# Setup
##### There are a few steps that you need to take in order to get this program working locally. The [settings.py](settings.py) file below has to be filled out correctly:

        

### 1) There are some mandatory fields that you need to fill out. If you don't fill these out, it will not work.

        # credentials for parent access
        PARENT_ACCESS_EMAIL  = ""
        PARENT_ACCESS_PASSWORD  = ""

        # either push, sms, or email
        NOTIFICATION_METHOD = "push"

        # in minutess
        REFRESH_INTERVAL = 1

        # school student id
        STUDENT_ID = ""

### 2) Now, you have to decide which notification mode you prefer. We currently support Twilio SMS, Gmail, or Spontit (recommended)
###
#### 2a) If you prefer to be notified via email, fill out the Gmail credentials fields. For the password, your normal google password will not work, and you have to create an [app specific password](https://support.google.com/mail/answer/185833?hl=en-GB), and enter that password into the ``` GMAIL_ACCOUNT_PASSWORD``` field:

    # gmail credentials
    GMAIL_ACCOUNT_EMAIL = # google account email
    GMAIL_ACCOUNT_PASSWORD = # app password
    
    # email you want to send notifications to
    DESTINATION_EMAIL =

#### If you prefer Email notifications, fill the ```PHONE_NUMBER_EMAIL ``` field with the destination email. If you would still like SMS notifications through email, you can look up your cellular carrier's extension to apply to the end of your phone number so that you can send emails to that email and have the emails be sent to your phone via SMS. If not, you can just fill this field out with the normal email that you would like these notifications to go to.
    
#### 2b) If you prefer to be notified via SMS, fill out the Twilio API keys fields along with the Twilio phone number fields:

    # twilio api keys
    TWILIO_ACCOUNT_SID = 
    TWILIO_AUTH_TOKEN = 
        
    # phone numbers for twilio
    TWILIO_PHONE_NUMBER = 
    DESTINATION_PHONE_NUMBER = 
#### The ``` TWILIO_ACCOUNT_SID ``` and the ``` TWILIO_AUTH_TOKEN ``` should be available in your [Twilio](https://twilio.com) dashboard. ```TWILIO_PHONE_NUMBER``` should be the phone number that Twilio assigns to you, and ``` DESTINATION_PHONE_NUMBER ``` should be your phone number.

#### 2c) If you want to be notified from Spontit's notification service, fill out your Spontit credentials:

    ###
    ### ONLY FILL OUT IF USING SPONTIT FOR NOTIFICATIONS (RECOMMENDED)
    ###

    SPONTIT_USERNAME = ""
    SPONTIT_SECCRET_KEY = ""
###

#### Now we have to update the array of classes in [settings.py](settings.py):

    classes = {
    
        "CLASS ONE": "XPATH ONE",
    
        "CLASS TWO": "XPATH TWO",
    
        "CLASS THREE": "XPATH THREE",
    
        "CLASS FOUR": "XPATH FOUR",
    
        "CLASS FIVE": "XPATH FIVE",
    
        "CLASS SIX": "XPATH SIX",
    
        "CLASS SEVEN": "XPATH SEVEN"
        
        }
        
#### Here, replace all of the ```CLASS XXX``` strings with the name of the course. This is completely up to you, and you can customize it to your liking. You can also add as many classes as you would like to track, and the program will track all of them.

###

#### In the second column, replace all of the ``` XPATH XXX ``` strings with the xpath of the grades in parent access. In order to do this, you need to inspect the element of your grades and right click on the element that shows your grade within the ``` <div> ``` tags. In the menu that shows up, you should see an option to copy which expands on hover. When expanded, one option should be to copy XPATH. It is imperative that you copy the right XPATHs for all of your classes, because these are the values that the program tracks. See the image below for how to copy the XPATH:

![Screenshot](https://github.com/siddharthlohani/genesis-grade-alerts/blob/main/Screen%20Shot%202021-03-01%20at%206.03.40%20PM.png)

#### After updating the class names and XPATHs of each course, it should look similar to this:

    classes = {
    
        "English 10H": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[1]/div",
    
        "AP US History": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr/td[1]/div",
    
        "Chem H": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td[3]/table/tbody/tr/td[1]/div",
    
        "Pre-Calc H": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[6]/td[3]/table/tbody/tr/td[1]/div",
    
        "Spanish V H": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[7]/td[3]/table/tbody/tr/td[1]/div",
    
        "AP CS A": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[8]/td[3]/table/tbody/tr/td[1]/div",
    
        "Physical Education": "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[10]/td[3]/table/tbody/tr/td[1]/div"
        
        }
        
#### Lastly, we need to install python and all necessary dependencies. This should be quick! Run the following commands to get all dependencies installed:

        pip3 install selenium
        pip3 install schedule
        pip3 install python-dotenv
        pip3 install twilio
        pip3 install spontit --upgrade && pip3 install requests
        
#### Installing Selenium:
##### Selenium is necessary to have in order to run this program, as it depends on the selenium functionality in order to fetch Genesis and get grades. First, make sure you have the selenium python package installed: ```pip install selenium```. You also need to have chrome driver installed (or the driver for the browser that you use). For Chrome, you can go to this [website](https://chromedriver.chromium.org/) to install it. Make sure that you have the driver in your PATH. You can follow [this tutorial](https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver) in order to do so. After this, the program should be ready to run! 

###

#### How to run:
#### Open a new terminal window in the folder which contains the files in this repo, and run ```python3 main.py```. This should run at the frequency that you specified in [.env](.env)! When your grades change, it will text you with your updated grades. It will be better if you have this program running 24/7, either through a web hosting service like [repl.it](https://repl.it) or on a computer you have lying around. A [Raspberry Pi](https://raspberrypi.org) is a great inexpensive computer that you can use as a local web server!

#### Questions:
#### If you have any questions, feel free to [email me](mailto:me@siddharthlohani.dev) or DM me on [Twitter](https://twitter.com/sidlohani)! If you do not have a computer which you can run this on, [email me](mailto:me@siddharthlohani.dev), and I can host it for you!

# About
#### Hi! I'm Sid, a Full Stack developer currently in High School. You can learn more about me on [my website](https://siddharthlohani.dev), or you can follow me on [Twitter](https://twitter.com/sidlohani)! If you found this project helpful, star it on Github!
