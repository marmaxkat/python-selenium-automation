from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# init driver
driver = webdriver.Chrome(executable_path='/Users/inna/Desktop/Automation/python-selenium-automation/chromedriver')
# driver.implicitly_wait(10)
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# # wait for 4 sec
# sleep(4)
driver.wait = WebDriverWait(driver, 10)
e = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))

# click search
e.click()

# verify
assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()
