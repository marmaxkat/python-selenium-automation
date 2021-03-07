from pages.base_page import Page
from selenium.webdriver.common.by import By

class ShoppingCart(Page):
    EMPTY_CART_MESSAGE = (By.XPATH, "//div[@id='sc-active-cart']//h2")

    def cart_is_empty(self, message):
        self.verify_text(message, *self.EMPTY_CART_MESSAGE)