from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon Product page')
def open_google(context):
    context.driver.get('https://www.amazon.com/dp/B07TJ51B6W/ref=cm_gf_axv_ihe_d_p0_qd0_6LQBgRNKLIJnobNSE9uU')


@when('Press Add to Cart Button')
def add_to_cart_btn_click(context):
    context.driver.find_element(By.ID, 'add-to-cart-button')


@then('Verify that the Product is in Shopping Cart')
def verify_product_in_sp(context):
    sp_subtotal = context.driver.find_element(By.CSS_SELECTOR, "span#sc-subtotal-label-buybox").text
    assert 'Subtotal (1 item)' in sp_subtotal, f'Expected "Subtotal (1 item)", but got {sp_subtotal }'
