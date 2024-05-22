from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import urllib.request
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

def openSeeMore(driver):
    seeMores = driver.find_elements(By.XPATH, "XPATH")
    if(len(seeMores) > 0):
        count = 0
        for i in seeMores:
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

def getBack(driver):
    if not driver.current_url.endswith('reviews'):
        driver.back()

def archive(driver, reviewList):
    driver.execute_script("window.scrollTo(0, -document.body.scrollheight);")
    time.sleep(10)

    for index, l in enumerate(reviewList):
        if(index % 10 == 0):
            driver.execute_script("arguments[0].scrollIntoView();", reviewList[0]) if index < 15 else driver.execute_script("arguments[0].scrollIntoView();", reviewList[index-15])
        time.sleep(1)
        try:
            driver.execute_script("arguments[0].scrollIntoView();", reviewList[index+15])
        except:
            driver.execute_script("arguments[0].scrollIntoView();", reviewList[-1])

        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", reviewList[index])
            
        for r in range(2):
            time.sleep(3)
            try:
                driver.execute_script("arguments[0].scrollIntoView();", reviewList[index+5])
                time.sleep(3)
            except:
                driver.execute_script("arguments[0].scrollIntoView();", reviewList[-1])
                driver.execute_script("arguments[0].scrollIntoView();", reviewList[index+r*3])
                time.sleep(3)
                with open(f'./PATH/{str(index)}_{r}.html',"w", encoding="utf-8") as file:
                    source_data = driver.page_source
                    bs_data = bs(source_data, 'html.parser')
                    file.write(str(bs_data.prettify()))
                    print(f'written: {index}_{r}')
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
    
    openSeeMore(driver) 
    getBack(driver)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    reviewList = driver.find_elements(By.XPATH, "XPATH FOR REVIEWS")
    numReviews = len(reviewList)
    if old_numReviews < numReviews:
        print()
    old_numReviews = numReviews

    # TERMINATE
    if numReviews >= numberReviews:
        archive(driver, reviewList)
        switch = False

with open(f'PATH TO FILE.html',"r", encoding="utf-8") as file:
    f = file.read()

page = bs(f, 'lxml')
reviews = page.find_all('div', {
    'class':'du4w35lb k4urcfbm l9j0dhe7 sjgh65i0'
                               })

ratings = []
users = []
usernames = []
texts = []
dates = []
for idx,r in enumerate(reviews):
    rating = r.find('h2',{"class":"gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl aahdfvyu hzawbc8m"}).get_text()
    try:
        ratings.append([i.strip() for i in rating.split('\n') if 'recommend' in i][0])
    except:
        ratings.append('no rating')

    users.append(r.find('a',{'class':'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p'}).get_text().strip())
    
    username = r.find('a',{'class':'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p'})\
                 .get('href')[25:].split('?')[0]
    if username == 'profile.php':
        username = r.find('a',{'class':'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p'})\
                 .get('href').split('?id=')[1].split('&')[0]
    usernames.append(username)
    
    text = r.find('span',{'class':'d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m'})
    if text is not None:
        texts.append(' '.join([i.strip() for i in text.get_text().split()]))
    else:
        text = r.find('div',{'class':'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql'})
        if text is not None:
            texts.append(text.get_text().strip())
        else:
            texts.append('no text')
            
    date = r.find('a',{'class':'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw'}).get('aria-label')
    if (' ' not in date) and ('h' in date):
        dates.append('October 1, 2021') #### REMEMBER TO CHANGE
    elif (' ' not in date) and ('d' in date):
        date0 = datetime.datetime.strptime('10/01/21', "%m/%d/%y")
        date1 = date0 - datetime.timedelta(days=int(date[0]))
        dates.append(date1)
    elif ('2020' in date) or ('2019' in date) or ('2018' in date):
        dates.append(date)
    else:
        dates.append(' '.join(date.split()[:2])+', 2021')

master = pd.DataFrame({
    'ratings':ratings, 
    'users':users,
    'usernames':usernames,
    'texts':texts,
    'dates':dates
                  })
