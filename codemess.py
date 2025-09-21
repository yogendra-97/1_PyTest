import time

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://www.naukri.com/nlogin/login?utm_source=google&utm_medium=cpc&utm_campaign=Brand&gad_source=1&gad_campaignid=19863995494&gbraid=0AAAAADLp3cE_eSpuT94XLmhYej5UiZGpf&gclid=EAIaIQobChMIke6rocrTjgMVEtIWBR3PFzQ0EAAYASAAEgLSvPD_BwE&gclsrc=aw.ds")
# driver.find_element(By.ID, "usernameField").send_keys("yogendranarayanp7799@gmail.com")
# driver.find_element(By.ID, "passwordField").send_keys("Yogi0522@GM2")
driver.find_element(By.XPATH,"//button[text()='Use OTP to Login']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter your 10 digit mobile number']").send_keys("")
time.sleep(20)
# 5 seconds is max time out. 2 seconds (3 seconds save)
driver.get("https://www.naukri.com/myapply/saveApply?strJobsarr=[290525900605]&acpPageType=S2J&applytype=single&src=S2J&logstr=d3skt0p-whtcv-0-F-0-1---&applySrc=whtcv-0-F-0-1---&multiApplyResp=%7B%22290525900605%22%3A200%7D&jobTitle=Software%20Dev%20Test%20Engineer")

results = driver.find_elements(By.XPATH,"//div/button[text()='Share Interest']")
y=len(results)
x=0
for x in range(y):
    driver.find_element(By.XPATH,"//div/button[text()='Share Interest']").click()
    time.sleep(3)

# for result in results:
#     result.find_element(By.XPATH,"div/button").click()

time.sleep(4)
#
# results = driver.find_elements(By.XPATH, "//div[@class='products']/div")#list[]
# count = len(results)
# assert count > 0
# for result in results:
#     result.find_element(By.XPATH,"div/button").click()
#
# driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()  #15
# driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#
# #Sum validation
# prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
# sum = 0
# for price in prices:
#    sum = sum + int(price.text)
#
# print(sum)
# totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
#
# assert sum == totalAmount
#
#
# driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# wait = WebDriverWait(driver,10)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
# print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
