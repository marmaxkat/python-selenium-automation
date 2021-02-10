from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_BOX = (By.CLASS_NAME, 'a-section')
COLOR_OPTION = (By.ID, 'color_name_1')


@when('Select color')
def add_to_cart_btn_click(context):
    context.driver.find_element(By.ID, 'add-to-cart-button')
    sleep(4)