from behave import *
from selenium.webdriver.common.by import By

PRODUCTS = (By.XPATH, "//li[@class='s-result-item' and .//span[contains(@class,'prime-price')]]/div")
PRODUCT_NAME = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name")


@then("Verify text ‘Regular’ and a product name are displayed")
def verify_name_and_text_displeed(context):
    product_elements = context.driver.find_elements(*PRODUCTS)
    for e in product_elements:
        assert 'Regular' in e.text, f'Error message....'
        product_name = e.find_element(PRODUCT_NAME)
        assert product_name, f'Product name is not there'
