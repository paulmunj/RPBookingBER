import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
from datetime import datetime

if __name__ ==  '__main__':
    options = Options()
    options.headless = True

    driver = uc.Chrome(options=options)
    driver.get('https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en')

    driver.find_element(By.CSS_SELECTOR, '#mainForm > div > div > div > div > div > div > div > div > div > div.div-text-content > div.text > div:nth-child(4) > a').click()
    time.sleep(8)
    driver.find_element(By.ID, 'xi-cb-1').click()

    time.sleep(5)
    driver.find_element(By.ID, 'applicationForm:managedForm:proceed').click()

    time.sleep(30)
    driver.find_element(By.CSS_SELECTOR, '#xi-sel-400>option[value="436"]').click()

    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#xi-sel-422>option[value="2"]').click()

    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#xi-sel-427>option[value="1"]').click()

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#xi-sel-428>option[value="436-0"]').click()


    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#xi-div-30 > div.ozg-kachel.kachel-436-0-1.level1 > label').click()

    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#inner-436-0-1 > div > div.ozg-accordion.accordion-436-0-1-1.level2 > label').click()

    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#inner-436-0-1 > div > div:nth-child(4) > div > div:nth-child(1) > label').click()

    time.sleep(10)
    driver.find_element(By.ID, 'applicationForm:managedForm:proceed').click()

    time.sleep(30)
    if "There are currently no dates" not in driver.page_source:
        url = 'https://api.telegram.org/<ABCD>/sendMessage' #Add the telegram BOT url
        payload =  '{"chat_id": "-100148965", "text": "Dates Available!!!!!", "disable_notification": false}'
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, data=payload, headers=headers)

    dt = datetime.now()
    f = open("C:\\Users\\OneDrive\\Documents\\RP\\log.txt", "a") # Maintain correct path for log
    dtenter = str(dt)+"\n"
    f.write(dtenter)
    f.close()

    time.sleep(10)

