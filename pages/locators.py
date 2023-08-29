from selenium.webdriver.common.by import By


class AdvertPageLocators:
    ADD_TO_FAVOURITE_BUTTON = (By.XPATH, "//*[contains(@class, 'add-favorite')]")


class FavouritePageLocators:
    FAVOURITE_IS_EMPTY = (By.XPATH, "//*[@data-marker='favorites-empty']/h3")
    FAVOURITE_IS_NOT_EMPTY = (By.XPATH, "//*[contains(@class, 'price-line-root-NiZHp')]")
