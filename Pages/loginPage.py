from selenium.webdriver.common.by import By
from Action.action import Events
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage(Events):
    profile = (By.XPATH, "//span[text()='Sign in']")
    sign_in = (By.XPATH, "//li[@id='listaccountNav-signIn']//a/child::span[text() = 'Sign in']")
    email_input = (By.XPATH, "//input[@name='username']")
    password_input = (By.XPATH, "//input[@name='password']")
    signIn_button = (By.XPATH, "//span[text()='Sign in']")
    h3_locator = (By.XPATH, "//span[text()='Please enter a valid password']")

    # Wait for the <h3> element to be present on the page
    def wait_for_h3_element(self, timeout=20):
        try:
            h3_locator_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.h3_locator))
            return h3_locator_element
        except TimeoutException:
            # Handle timeout exception if needed
            print("Timed out waiting for h3 element to be present.")
            return None

    def __init__(self, driver):
        super().__init__(driver)

    def click_login(self, email, password):
        self.do_click(self.profile)
        self.do_click(self.sign_in)
        self.do_send_keys(self.email_input, email)
        self.do_send_keys(self.password_input, password)
        self.do_click(self.signIn_button)


