from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
SIZE_OPTION_0 = (By.ID, 'size_name_0')


@when('Select shoes size')
def select_size(context):
    context.driver.find_element(*SIZE_SELECTION_BTN).click()
    context.driver.find_element(*SIZE_OPTION_0).click()
    sleep(4)


@when('Click on Add to cart button')
def add_to_cart_btn_click(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    assert expected_count == cart_count, f'Expeced {expected_count} items, but got {cart_count} items'
