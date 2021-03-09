from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Click on first product')
def click_first_product(context):
    context.app.search_result_page.click_on_product()
