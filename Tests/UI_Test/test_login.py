import pytest
from Tests.UI_Test.BaseTest import BaseTest
from Pages.loginPage import LoginPage
from Tests.configtest import init_driver, login_data, assertion_data


class Test_Login(BaseTest):

    @pytest.mark.run(order=1)
    def test_invalidPassword(self, init_driver, login_data, assertion_data):
        driver = init_driver
        loginPage = LoginPage(init_driver)
        loginPage.click_login(login_data['EMAIL'], login_data['INVALID PASSWORD'])
        assert loginPage.wait_for_h3_element().text in assertion_data['expected_text']
        assert assertion_data['title'] in driver.title

    @pytest.mark.run(order=2)
    def test_valid_signIn(self, init_driver, login_data, assertion_data):
        driver = init_driver
        loginPage = LoginPage(init_driver)
        loginPage.click_login(login_data['EMAIL'], login_data['PASSWORD'])
        assert driver.current_url == assertion_data['expected_url']
