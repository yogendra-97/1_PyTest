
import selenium
from SeleniumLibrary.keywords import window
from selenium import webdriver
from selenium.common import NoSuchAttributeException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.browserstack.com/release-notes")
time.sleep(5)
driver.execute_script("window.scrollBy(0,1);")
ls= driver.find_elements(By.XPATH, "//div[@role='listitem']")
print(type(ls))
print(len(ls))
print(ls)

try:
    for element in ls[0:9]:
        date = element.find_element(By.XPATH, "div/span").text
        print(date)
except Exception as e:
    print(e)