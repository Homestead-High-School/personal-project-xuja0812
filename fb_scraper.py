from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import urllib.request
import pandas as pd
import json
import time
import re
import datetime

def openComment(driver):
    moreComment = driver.find_elements(By.XPATH, "XPATH")
    if(len(moreComment) > 0):
        count = 0
        for i in moreComment:
            actions = ActionChains(driver)
            try:
                actions.move_to_element(i).click().perform()
                count+=1
            except:
                try:
                    driver.execute_script("arguments[0].click();", i) # MANIPULATES DOM IN JS INSTEAD OF ACTIONS
                    count+=1
                except:
                    continue
        time.sleep(1)
    else:
        pass

# SAME IMPLEMENTATION AS THE openComment FUNCTION JUST WITH A DIFFERENT XPATH
def openReply(driver):
    replies = driver.find_elements(By.XPATH, "XPATH")
    if(len(replies) > 0):
        count = 0
        for i in replies:
            actions = ActionChains(driver)
            try:
                actions.move_to_element(i).click().perform()
                count+=1
            except:
                try:
                    driver.execute_script("arguments[0].click();", i) # MANIPULATES DOM IN JS INSTEAD OF ACTIONS
                    count+=1
                except:
                    continue
        time.sleep(1)
    else:
        pass

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

cService = webdriver.ChromeService(executable_path='/Users/15423/Downloads/chromedriver-mac-x64/chromedriver')
driver = webdriver.Chrome(service = cService, options = chrome_options)

with open("fb_credentials.txt") as file:
    EMAIL = file.readline().split['""'][1]
    PASSWORD = file.readline().split['""'][1]

# LOGS INTO FACEBOOK USING INFORMATION FROM THE TEXT FILE
driver.get("http://facebook.com")
wait = WebDriverWait(driver, 30)
email_element = wait.until(EC.visibility_of_element_located(By.NAME('email')))
email_element.send_keys(EMAIL)
password_element = wait.until(EC.visibility_of_element_located(By.NAME('password')))
password_element.send_keys(PASSWORD)
password_element.send_keys(Keys.RETURN)

# RETRIEVES ANY PAGE ONCE THE USER IS LOGGED IN
time.sleep(5)
driver.get('URL')
time.sleep(5)

# UNFOLDS ALL THE ELEMNENTS ON THE PAGE BY OPENING REPLIES AND COMMENTS AND SCROLLING TO THE END OF THE PAGE
count = 0
switch = True
old_numReviews = 0
numberReviews = 999

while(switch):
    count+=1
    openComment(driver)
    getBack(driver)

    for i in range(3):
        openReply(driver)
        getBack(driver)
    
    for i in range(3):
        openReply(driver)
        getBack(driver)
    
    openSeeMore(driver) # SAME IMPLEMENTATION WITH DIFFERENT XPATH
    getBack(driver)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # FIGURE OUT A WAY FOR IT TO END THE SCRIPT
    # IF WE OBTAIN THE NUMBER OF REVIEWS WE WANT WE TERMINATE
