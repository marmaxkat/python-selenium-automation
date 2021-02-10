from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[./span[@class='a-price']]")


@when ('Click on first product')
def click_first_product(conext):
    sleep(4)
    conext.driver.find_element(*PRODUCT_RESULT).click()



