from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on the cart icon')
def click_sp_icon(context):
    context.app.amazon_top_menu.click_sc_icon()


@then('Verify that Shopping Cart is empty')
def verify_sp_empty(context):
    context.app.shopping_cart_page.cart_is_empty('Your Amazon Cart is empty')