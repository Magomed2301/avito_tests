from pages.advert_page import AdvertPage
from pages.favourites_page import FavouritesPage


class TestAdvertPage:
    advert_link = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
    favourites_link = "https://www.avito.ru/favorites"

    def test_favourites_is_empty(self, browser):
        page = FavouritesPage(browser, self.favourites_link)
        page.open()
        page.should_be_favourites_is_empty()

    def test_add_to_favourite(self, browser):
        page = AdvertPage(browser, self.advert_link)
        page.open()
        page.add_to_favourite()

    def test_favourites_is_not_empty(self, browser):
        page = FavouritesPage(browser, self.favourites_link)
        page.open()
        page.should_be_favourites_is_not_empty()
