from selenium.webdriver.common.by import By
from behave import when, then

HAM_MENU = (By.ID,'nav-hamburger-menu')


@then('Verify hamburger menu icon is visible')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)
    context.driver.refresh()
    context.driver.find_element(*HAM_MENU).click()


@when('Click to open Amazon Hamburger Menu')
def click_ham_menu(context):
    context.driver.find_element(*HAM_MENU).click()
