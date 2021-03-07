from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()

@when('Verify user logged out')
def verify_user_logged_out(context):
    context.app.amazon_top_menu.verify_user_logged_out()


@when('Click Orders')
def click_orders_button(context):
    context.app.amazon_top_menu.click_order_button()

@then('Verify Sign in page opened')
def verify_sign_in_page_opened(context):
   context.app.sign_in_page.verify_title_text('Sign-In')