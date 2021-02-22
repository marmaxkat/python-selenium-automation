from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@given('Open Amazon Best Sellers page')
def open_bs_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@given('Open Amazon Prime page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@given('Open Amazon Wholefoods page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@given('Open Amazon Dress B07K16R9V3 page')
def open_amazon_B07K16R9V3_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07JZTT5LX')


@given('Open Amazon Wrond Product page')
def open_amazon_B07K16R9V3_page(context):
    context.driver.get('https://www.amazon.com/dkfkf')


@given("Open Amazon {url_query} page")
def open_product_page(context, url_query):
    context.driver.get(url_query)