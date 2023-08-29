from .base_page import BasePage
from .locators import AdvertPageLocators


class AdvertPage(BasePage):
    def add_to_favourite(self):
        self.browser.find_element(*AdvertPageLocators.ADD_TO_FAVOURITE_BUTTON).click()
