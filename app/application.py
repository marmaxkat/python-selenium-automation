from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.amazon_top_menu import TopMenu
from pages.sign_in_page import SignIn
from pages.shopping_cart_page import ShoppingCart


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.amazon_top_menu = TopMenu(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.shopping_cart_page = ShoppingCart(self.driver)

