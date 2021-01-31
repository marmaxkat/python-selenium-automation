from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input Watches into Amazon search field')
def input_search(context):
    search_field = context.driver.find_element(By.ID,'twotabsearchtextbox')
    search_field.send_keys('Watches')

@when('Click on Amazon search icon')
def click_amazon_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then('Product results for Watches are shown')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_text = '"Watches"'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@then('Page URL has Wathes in it')
def verify_url_contents_query(context):
    assert 'Watches' in context.driver.current_url, f'Watches not in {context.driver.current_url}'
