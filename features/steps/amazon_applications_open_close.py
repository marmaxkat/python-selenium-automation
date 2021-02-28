from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher("re")

AMAZON_APP_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/gp/feature.html?docId=1000625601']")
SEND_LINK_BTN = (By.CSS_SELECTOR, "input[aria-labelledby='mgt-email-sms-send-button-announce']")


@step('Click on Amazon applications link')
def step_impl(context):
    context.driver.find_element(*AMAZON_APP_LINK).click()


@then('Amazon app page is opened')
def step_impl(context):
    context.driver.find_element(*SEND_LINK_BTN)



