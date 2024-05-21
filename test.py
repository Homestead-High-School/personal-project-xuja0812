from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

cService = webdriver.ChromeService(executable_path='/Users/15423/Downloads/chromedriver-mac-x64/chromedriver')
driver = webdriver.Chrome(service = cService, options = chrome_options)
driver.get('https://hoopshype.com/salaries/players/')
players = driver.find_elements(By.XPATH, '//td[@class="name"]')

players_list = []
print(len(players))
for p in range(len(players)):
    if(players[p].text != ""):
        players_list.append(players[p].text)

salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]')
salaries_list = []
for p in range (len(salaries)):
    if(players[p].text != ""):
        salaries_list.append(salaries[p].text)

df = pd.DataFrame(columns=['Year','Player','Salary'])
data_tuples = list(zip(players_list[1:],salaries_list[1:]))
temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary'])
temp_df['Year'] = 2023
df = pd.concat([df, temp_df])

print(df)
driver.close()
