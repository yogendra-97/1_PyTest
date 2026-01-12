from selenium.webdriver.common.by import By


def test_google(browser):
    browser.get("https://www.google.com")
    browser.find_element(By.ID, "APjFqb").sendkeys("12345564564363")