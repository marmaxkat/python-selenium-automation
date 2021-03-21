from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    FIRST_PRODUCT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[./span[@class='a-price']]")
    SELECTED_DEPARTMENT_CATEGORY = (By.CSS_SELECTOR, "#nav-subnav[data-category='{DPT_SBSTR}']")

    def verify_search_result(self, result_word):
        self.verify_text(result_word, *self.RESULT)

    def click_on_product(self):
        self.click(*self.FIRST_PRODUCT)

    def _get_locator(self, departments: str):
        return [self.SELECTED_DEPARTMENT_CATEGORY[0], self.SELECTED_DEPARTMENT_CATEGORY[1].replace('{DPT_SBSTR}', departments)]

    def verify_department(self, departments):
        locator = self._get_locator(departments)
        self.wait_for_element_appear(*locator)