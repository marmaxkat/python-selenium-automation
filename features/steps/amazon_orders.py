from behave import given, when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Verify user logged out')
def verify_user_logged_out(context):
    sign_text = context.driver.find_element(By.XPATH, "//div[contains(@class,'nav-line-1-container')]").text
    assert 'Hello, Sign in' in sign_text


@when('Click Orders')
def click_orders_button(context):
    orders_button = context.driver.find_element(By.ID, 'nav-orders')
    orders_button.send_keys(Keys.ENTER)

@then('Verify Sign in page opened')
def verify_sign_in_page_opened(context):
    sign_in_text = context.driver.find_element(By.XPATH, "//h1[contains(@class,'a-spacing-small')]").text
    assert 'Sign-In' in sign_in_text
