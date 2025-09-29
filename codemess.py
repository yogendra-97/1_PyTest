import time

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://www.naukri.com/nlogin/login?utm_source=google&utm_medium=cpc&utm_campaign=Brand&gad_source=1&gad_campaignid=19863995494&gbraid=0AAAAADLp3cE_eSpuT94XLmhYej5UiZGpf&gclid=EAIaIQobChMIke6rocrTjgMVEtIWBR3PFzQ0EAAYASAAEgLSvPD_BwE&gclsrc=aw.ds")
driver.find_element(By.XPATH,"//button[text()='Use OTP to Login']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter your 10 digit mobile number']").send_keys("")
time.sleep()
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
driver.close()