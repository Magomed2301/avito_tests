from .base_page import BasePage
from .locators import FavouritePageLocators


class FavouritesPage(BasePage):
    def should_be_favourites_is_empty(self):
        expected_value = 'Сохраняйте объявления'
        actual_value = self.browser.find_element(*FavouritePageLocators.FAVOURITE_IS_EMPTY).text
        assert expected_value == actual_value, "Текст не совпадает, {}".format(actual_value)

    def should_be_favourites_is_not_empty(self):
        expected_value = '555'
        actual_value = self.browser.find_element(*FavouritePageLocators.FAVOURITE_IS_NOT_EMPTY).text
        assert expected_value in actual_value, "Текст не совпадает, {}".format(actual_value)
