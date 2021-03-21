from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    CART = (By.ID, 'nav-cart-count')
    SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
    SIZE_SELECTION_BTN = (By.ID, 'native_dropdown_selected_size_name')
    SIZE_OPTION_0 = (By.ID, 'size_name_0')
    PRICE_BY_BOX = (By.ID, 'unifiedPrice_feature_div')
    COLOR_OPTION = (By.ID, 'color_name_0')
    NEW_ARRIVALS_LINK = (By.CSS_SELECTOR, '#nav-subnav > a:nth-child(7)')
    NEW_ARRIVALS_PRODUCTS = (By.CSS_SELECTOR, 'a.mm-merch-panel>ul>li')

    def hover_add_to_cart_btn(self):
        add_to_cart_btn = self.find_element(*self.ADD_TO_CART_BTN)
        action = ActionChains(self.driver)
        action.move_to_element(add_to_cart_btn)
        action.perform()


    def click_add_to_cart(self):
        self.wait_for_element_appear(*self.ADD_TO_CART_BTN)
        self.click(*self.ADD_TO_CART_BTN)

    def select_color(self):
        self.wait_for_element_click(*self.COLOR_OPTION)
        self.click(*self.COLOR_OPTION)

    def select_size(self):
        self.click(*self.SIZE_SELECTION_BTN)
        self.click(*self.SIZE_OPTION_0)
        self.wait_for_element_appear(*self.PRICE_BY_BOX)

    def hover_add_to_cart_btn(self):
        add_to_cart_btn = self.find_element(*self.ADD_TO_CART_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(add_to_cart_btn)
        actions.perform()
        from time import sleep
        sleep(5)

    def hover_new_arrivals_link(self):
        new_arrivals_link = self.find_element(*self.NEW_ARRIVALS_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals_link)
        actions.perform()
        from time import sleep
        sleep(5)


    def verify_cart_count(self, expected_count):
        self.verify_text(expected_count, *self.CART)


    def verify_size_selection_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_TOOLTIP)


    def verify_new_arrivals_products(self):
        na_products = self.driver.find_elements(*self.NEW_ARRIVALS_PRODUCTS)
        for e in na_products:
            assert 'See More' in e.text, f'Error message....'


