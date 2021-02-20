from behave import *
from selenium.webdriver.common.by import By

PRODUCT_BLOCS = (By.CSS_SELECTOR, ".s-result-list li.s-result-item div[class='s-item-container']")
PRODUCT_NAME = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")


@then("Verify text ‘Regular’ and a product name are displayed")
def verify_name_and_text_displeed(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify text ‘Regular’ and a product name are displayed')