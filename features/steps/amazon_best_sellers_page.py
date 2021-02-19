from selenium.webdriver.common.by import By
from behave import given, when, then


BS_PAGE_TOP_LINKS =(By.CSS_SELECTOR, "#zg_tabs a")


@then('Verify there are 5 links')
def verify_links(context, expected_links):
    actual_links = context.driver.find_elements(*BS_PAGE_TOP_LINKS)
    assert len(actual_links) == expected_links, f'{len(actual_links)} boxes shown instead of {expected_links}'
