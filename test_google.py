import selenium

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.suppip install seleniumport.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait

def test_Apple(browser):

    browser.get("https://www.google.com/")
    browser.find_element(By.ID, "APjFqb").send_keys('Google_Test')
    time.sleep(2)

    driver = browser
    
    driver.find_element(By.NAME, "btnK").click()
    time.sleep(2)