from selenium.webdriver.common.by import By
from behave import given, when, then


BS_PAGE_TOP_LINKS =(By.CSS_SELECTOR, "div#zg_tabs>ul>li")


@given('Open Amazon Best Sellers page')
def open_bs_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are 5 links')
def verify_links(context):
    present_links = context.driver.find_elements(*BS_PAGE_TOP_LINKS)
    assert len(present_links) == 5, f'{len(present_links)} boxes shown instead of 5'
