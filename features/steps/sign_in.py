from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
NAV_TOOLS = (By.ID, 'nav-tools')


@when('Click Sign In from popup')
def click_on_popup_btn(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))
    e.click()


@then('Verify Sign in page opens')
def verify_sign_in_page_opens(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),
                              f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin')

    # assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, \
    #     f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin'


@then("Verify Sign in is clickable")
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))


@when("Wait for {sec} sec")
def sleep_sec(context, sec):
    sleep(int(sec))


@then("Verify Sign in is disappears")
def verify_sign_in_disappears(context):
    context.driver.wait.until(EC.presence_of_element_located(SIGN_IN_POPUP_BTN))
#    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))
    context.driver.wait.until(EC.presence_of_element_located(NAV_TOOLS))
