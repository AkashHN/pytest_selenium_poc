from Tests.UI_Test.BaseTest import BaseTest
from Pages.homePage import HomePage
from Tests.configtest import init_driver, assertion_data
import pytest


class Test_Home(BaseTest):
    @pytest.mark.run(order=3)
    def test_product_search(self, init_driver, assertion_data):
        homePage = HomePage(init_driver)
        homePage.search_product(assertion_data["product_name"])
        homePage.sort_products_by_bestseller()
        product_title_in_home = homePage.get_product_title()
        homePage.select_product()
        product_title_in_discription = homePage.get_product_title_in_product_discription()
        # assert product_title_in_home == product_title_in_discription
        homePage.add_product_to_cart()
        cart_heading = homePage.get_cart_shipping_headline()
        assert cart_heading == assertion_data["cart_heading"]
        homePage.close_cart()
        homePage.cart_logo()

