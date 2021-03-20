from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@given('Open Amazon')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Input {search_query} into Amazon search field')
def input_amazon_search(context, search_query):
    context.app.main_page.input_amazon_search(search_query)


@when('Seasch for {search_query}')
def input_amazon_search(context, search_query):
    context.app.main_page.input_amazon_search(search_query)
    context.app.main_page.click_search_amazon()


@when('Click on Amazon search icon')
def click_amazon_icon(context):
    context.app.main_page.click_search_amazon()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.main_page.select_department(alias)


@then('Product results for {result_word} are shown successfully')
def verify_search_result(context, result_word):
    context.app.search_result_page.verify_search_result(result_word)


@then('Page URL has {query} in it')
def verify_url_contains_query(context, query):
    context.app.main_page.verify_url_contains_query(query)


@then('Verify books department is selected')
def verify_department(context):
    context.app.search_result_page.verify_department()
