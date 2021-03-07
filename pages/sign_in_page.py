from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignIn(Page):
    SIGN_IN_TITLE = (By.CSS_SELECTOR, 'h1')

    def verify_title_text(self, result_word):
        self.verify_text(result_word, *self.SIGN_IN_TITLE)