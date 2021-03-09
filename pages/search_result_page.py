from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    FIRST_PRODUCT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[./span[@class='a-price']]")

    def verify_search_result(self, result_word):
        self.verify_text(result_word, *self.RESULT)

    def click_on_product(self):
        self.click(*self.FIRST_PRODUCT)