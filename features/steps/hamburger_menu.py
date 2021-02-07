from selenium.webdriver.common.by import By
from behave import given, when, then

HAM_MENU = (By.ID,'nav-hamburger-menu')

@then('Verify hamburger menu icon visible')
def verify_ham_menu_present(context):
    print('Find Element')
    element=context.driver.find_element(*HAM_MENU)
    print(element)
    print(type(element))

    print('Find Elements')
    elements = context.driver.find_elements(*HAM_MENU)
    print(elements)
    print(type(elements))

    assert len(elements) == 1