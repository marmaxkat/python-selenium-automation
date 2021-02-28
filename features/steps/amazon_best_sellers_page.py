from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
import time


BS_PAGE_TOP_LINKS = (By.CSS_SELECTOR, "#zg_tabs a")
BS_LINK = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers_22595f4f23134e4aa687cca616dd2701']")


@when('Click on Best Sellers link')
def click_bs_link(context):
    context.original_window = context.driver.window_handles[0]
    context.driver.find_element(*BS_LINK).click()
    time.sleep(5)
    original_window_title = context.driver.title
    print(original_window_title)



@when('Store BS window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)



@then('Clicks on each top link and verify that new page opens')
def click_on_top_links(context):
    top_links = context.driver.find_elements(*BS_PAGE_TOP_LINKS)
    num_links = len(top_links)
    for link in range(0, num_links):
        context.driver.wait.until(EC.element_to_be_clickable(top_links[link]))
        top_links[link].click()
        context.driver.wait.until(EC.new_window_is_opened)
        context.driver.switch_to.window(context.driver.window_handles[link])
        new_window_title = context.driver.title
        print(new_window_title)

        context.driver.close()
        context.driver.switch_to.window(context.original_window)


# @then('Verify there are 5 links')
# def verify_links(context, expected_links):
#     actual_links = context.driver.find_elements(*BS_PAGE_TOP_LINKS)
#     assert len(actual_links) == expected_links, f'{len(actual_links)} boxes shown instead of {expected_links}'
