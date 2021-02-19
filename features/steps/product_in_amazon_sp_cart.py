from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTION = (By.ID, 'color_name_1')


@when('Select color')
def add_to_cart_btn_click(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(COLOR_OPTION))
    e.click()
    # sleep(4)