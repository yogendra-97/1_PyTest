import time

from selenium.webdriver.common.by import By


def test_google(browser):
    browser.get("https://www.google.com")
    browser.find_element(By.XPATH, "//*[@id='APjFqb']").send_keys("12345564564363")
    time.sleep(5)
