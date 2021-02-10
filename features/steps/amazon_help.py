from selenium.webdriver.common.by import By
from behave import given, when, then


FIRST_HEADLINE = (By.CSS_SELECTOR, "div.a-section>h1")
HELP_BOXES_HEADLINE = (By.CSS_SELECTOR, "div.a-section>h2")
HELP_BOXES = (By.CSS_SELECTOR, "div.self-service-rich-card")
HELP_SEARCH = (By.CSS_SELECTOR, "input#helpsearch")
HELP_TOPICS_HEADLINE = (By.CSS_SELECTOR, "div.a-span12>h1")
TOPICS_LIST = (By.CSS_SELECTOR, "ul#category-section>li.csg-category")
HELP_TOPICS_IMG = (By.CSS_SELECTOR, "img.csg-hb-promo")


@then("Verify UI elements are present")
def element_present(context):
    context.driver.find_element(*FIRST_HEADLINE)
    context.driver.find_element(*HELP_BOXES_HEADLINE)
    help_boxes = context.driver.find_elements(*HELP_BOXES)
    assert len(help_boxes) == 8, f'{len(help_boxes)} boxes shown instead of 8'
    context.driver.find_element(*HELP_SEARCH)
    context.driver.find_element(*HELP_TOPICS_HEADLINE)
    topics_list = context.driver.find_elements(*TOPICS_LIST)
    assert len(topics_list) == 12, f'{len(topics_list)} topics shown instead of 12'
    help_topics_img = context.driver.find_elements(*HELP_TOPICS_IMG)
    assert len(help_topics_img) == 8, f'{len(help_topics_img)} topic boxes images shown instead of 8'

