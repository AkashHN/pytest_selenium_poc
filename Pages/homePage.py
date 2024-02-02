from selenium.webdriver import Keys

from Action.action import Events
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage(Events):
    searchArea_locator = (By.XPATH, "//input[@id='search']")
    sortBtn_locator = (By.XPATH, "//div[text()='Sort']//ancestor::button")
    bestSellerRadioBtn_locator = (By.XPATH, "//input[@id='bestselling-best seller']")
    apply_button_locator = (By.XPATH, "//button[text()='Apply']")
    selectItem_locator = (By.XPATH, "(//section/div/div[2]//a)[2]")
    productText_locator = (By.XPATH, "//h1[@id='pdp-product-title-id']")
    addToCart_locator = (By.XPATH, "//button[@id='addToCartButtonOrTextIdFor89807551']")
    shippingText_locator = (By.XPATH, "//h3[text()='Shipping']")
    closeCartPopUp_locator = (By.XPATH, "//button[@aria-label='close']")
    cart_logo_locator = (By.XPATH, "((//span[contains(text(),'Sign')])[1]/following::div)[1]")
    sign_out_locator = (By.XPATH, "//span[text()='Sign Out']")

    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self, product_name):
        self.do_send_keys(self.searchArea_locator, product_name)
        self.do_send_keys(self.searchArea_locator, Keys.RETURN)

    def sort_products_by_bestseller(self):
        self.scroll_to_element(self.sortBtn_locator)
        self.driver.execute_script(f"window.scrollBy(0, 40);")
        self.do_click(self.sortBtn_locator)
        if not self.driver.find_element(By.XPATH, "//input[@id='bestselling-best seller']").is_selected():
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.bestSellerRadioBtn_locator))
            self.do_click(self.bestSellerRadioBtn_locator)
        self.do_click(self.apply_button_locator)

    def get_product_title(self):
        self.scroll_to_element(self.selectItem_locator)
        self.driver.execute_script(f"window.scrollBy(0, 500);")
        return self.get_element_text(self.selectItem_locator)

    def select_product(self):
        self.scroll_to_element(self.selectItem_locator)
        self.driver.execute_script(f"window.scrollBy(0, 500)")
        self.do_click(self.selectItem_locator)

    def get_product_title_in_product_discription(self):
        return self.get_element_text(self.productText_locator)

    def add_product_to_cart(self):
        self.scroll_to_element(self.addToCart_locator)
        self.driver.execute_script(f"window.scrollBy(0, 500);")
        self.do_click(self.addToCart_locator)

    def get_cart_shipping_headline(self):
        return self.get_element_text(self.shippingText_locator)

    def close_cart(self):
        self.do_click(self.closeCartPopUp_locator)

    def cart_logo(self):
        self.do_click(self.cart_logo_locator)

    def sign_out(self):
        self.do_click(self.sign_out_locator)