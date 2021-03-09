from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    CART = (By.ID, 'nav-cart-count')

    COLOR_OPTION = (By.ID, 'color_name_0')

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def select_color(self):
        self.wait_for_element_click(*self.COLOR_OPTION)
        self.click(*self.COLOR_OPTION)

    def verify_cart_count(self, expected_count):
        self.verify_text(expected_count, *self.CART)


