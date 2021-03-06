from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from behave import given, when, then
from time import sleep

SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
SIZE_OPTION_0 = (By.ID, 'size_name_0')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@when('Select color')
def select_watch_color(context):
    context.app.product_page.select_color()


@when('Select shoes size')
def select_size(context):
    context.app.product_page.select_size()


@when('Hover over Add to Cart button')
def hover_add_to_cart_btn(context):
    context.app.product_page.hover_add_to_cart_btn()


@when('Hover over New Arrivals link')
def hover_new_arrivals_link(context):
    context.app.product_page.hover_new_arrivals_link()


@when('Click on Add to cart button')
def add_to_cart_btn_click(context):
    context.app.product_page.click_add_to_cart()


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    context.app.product_page.verify_cart_count(expected_count)


@then('Verify user can click through color')
def verify_can_select_colors(context):
    expected_colors = ['Emerald', 'Ivory', 'Navy']
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[i] == selected_color, f'Expected {expected_colors[i]}, but got {selected_color}'


@then("Verify user can click through {color_list} colors")
def verify_can_select_colors(context, color_list):
    expected_colors = list(color_list.split(","))
    print(expected_colors)
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        print(expected_colors[i])
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[i] == selected_color, f'Expected {expected_colors[i]}, but got {selected_color}'


@then('Verify size selection tooltip is shown')
def verify_size_selection_tooltip(context):
    context.app.product_page.verify_size_selection_tooltip()


@then('Verify users can see the deals')
def verify_new_arrivals_products(context):
    context.app.product_page.verify_new_arrivals_products()