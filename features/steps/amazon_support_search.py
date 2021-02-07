from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

SEARCH_HELP_INPUT = (By.XPATH, "//input[@id='helpsearch']")
ENTER_BTN = (By.XPATH, "//input[@type='search']")
RESULTS = (By.XPATH, "//div[contains(@class,'help-content')]/h1")

@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get(' https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search text} into search field')
def input_support_search(context, search_text):
    search_field = context.driver.find_element(*SEARCH_HELP_INPUT)
    search_field.send_keys(search_text)
    sleep(4)


@when('Click Enter')
def click_enter(context):
    context.driver.find_element(*ENTER_BTN).send_keys(Keys.ENTER)
    sleep(1)


@then('Verify that {result_text} text is present')
def verify_cancel_order_text(context, search_text, result_text):
    results_msg = context.driver.find_element(*RESULTS).text
    assert search_text in result_text, "Expected word '{}' in message, but got '{}'".format(search_text, result_text)