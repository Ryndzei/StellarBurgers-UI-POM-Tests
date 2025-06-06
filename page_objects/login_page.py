from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators
from locators.login_account_locators import LoginAccountLocators
from page_objects.base_page import BasePage
from urls import URL


class LoginPage(BasePage):

    def click_forgot_password_button(self):
        self.safe_click(LoginAccountLocators.PASSWORD_RECOVERY_BUTTON)

    def set_email(self, email):
        self.safe_click(LoginAccountLocators.LOGIN_EMAIL_INPUT)
        self.find_element(LoginAccountLocators.LOGIN_EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.safe_click(LoginAccountLocators.LOGIN_PASSWORD_INPUT)
        self.find_element(LoginAccountLocators.LOGIN_PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.safe_click(LoginAccountLocators.LOGIN_BUTTON)

    def wait_until_url_to_be_login_page(self, timeout=15):
        self.wait_until(ec.url_to_be(URL.LOGIN_URL), timeout)
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)