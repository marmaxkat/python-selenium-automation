from selenium.webdriver.common.by import By
from behave import given, when, then


BENEFIT_BOXES = (By.CSS_SELECTOR, '.benefit_box')


@given('Open Amazon Prime page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify {expected_boxes} benefit boxes are displayed')
def verify__boxes_(context, expected_boxes):
    actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(actual_boxes) == expected_boxes, f'Expected {expected_boxes}, but we see {len(actual_boxes)}'


