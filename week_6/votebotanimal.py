from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


web = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # opens google.
web.get('https://docs.google.com/forms/d/e/1FAIpQLScXNbdAs0HF9d5DHFXo1qTjK9wMSrG1nBCb1lzFw0tkJUGvOw/viewform')
while 0 == 0:
    l = web.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    l.send_keys("Diana_Noah@student.mahoningctc.com")
    l.send_keys(Keys.RETURN)
    k = web.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    k.send_keys("Jeff")
    k.send_keys(Keys.RETURN)
    j = web.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')
    j.click
    h = web.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    h.click
    time.sleep(5000)