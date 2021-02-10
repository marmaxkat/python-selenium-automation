from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {search_query} into Amazon search field')
def input_amazon_search(context, search_query):
    search_field = context.driver.find_element(*SEARCH_FIELD)
    search_field.send_keys(search_query)
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on Amazon search icon')
def click_amazon_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@then('Product results for {result_word} are shown successfully')
def verify_search_result(context, result_word):
    actual_text = context.driver.find_element(*RESULT).text
    expected_text = f'{result_word}'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@then('Page URL has {query} in it')
def verify_url_contents_query(context, query):
    assert query in context.driver.current_url, f'{query} in {context.driver.current_url}'
