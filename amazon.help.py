from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome('chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search_field = driver.find_element(By.ID, 'helpsearch')
search_field.send_keys('Cancel order')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.XPATH, "//input[@type='search']").send_keys(Keys.ENTER)

# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[contains(@class,'help-content')]").text

driver.quit()