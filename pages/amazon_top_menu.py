from pages.base_page import Page
from selenium.webdriver.common.by import By

class TopMenu(Page):
    SIGN_IN_TEXT = (By.XPATH, "//div[contains(@class,'nav-line-1-container')]")
    ORDER_BUTTON = (By.ID, 'nav-orders')
    SHOPPING_CART_ICON = (By.ID, 'nav-cart')

    def verify_user_logged_out(self):
        self.verify_text('Hello, Sign in', *self.SIGN_IN_TEXT)

    def click_order_button(self):
        self.click(*self.ORDER_BUTTON)

    def click_sc_icon(self):
        self.click(*self.SHOPPING_CART_ICON)



