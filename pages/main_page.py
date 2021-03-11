from pages.base_page import Page
from support.environment import ENV
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')

    def open_main_page(self):
        self.open_url()

    def input_amazon_search(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)

    def click_search_amazon(self):
        self.click(*self.SEARCH_ICON)

