from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[./span[@class='a-price']]")


@when('Click on first product')
def click_first_product(conext):
    # sleep(4)
    # conext.driver.find_element(*PRODUCT_RESULT).click()
    e = conext.driver.wait.until(EC.element_to_be_clickable(PRODUCT_RESULT))
    e.click()



