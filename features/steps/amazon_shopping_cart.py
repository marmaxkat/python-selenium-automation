from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on the cart icon')
def click_sp_icon(context):
    context.driver.find_element(By.XPATH, "//a[@id='nav-cart']").click()


@then('Verify that Shopping Cart is empty')
def verify_sp_empty(context):
    empty_sp_text = context.driver.find_element(By.XPATH, "//div[@id='sc-active-cart']//h2").text
    assert 'Your Amazon Cart is empty' in empty_sp_text, f"Your Amazon Cart is empty' is not in '{empty_sp_text}'"
