from selenium.webdriver.common.by import By
from behave import given, when, then


BENEFIT_BOXES = (By.CSS_SELECTOR, '.benefit-box')


@then('Verify {expected_boxes} benefit boxes are displayed')
def verify_boxes(context, expected_boxes):
    actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(actual_boxes) == int(expected_boxes), f'Expected {expected_boxes}, but we see {len(actual_boxes)}'
