from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators
from locators.forgot_password_locators import ForgotPasswordLocators
from page_objects.base_page import BasePage
from random_data import random_email
from urls import URL


class ForgotPasswordPage(BasePage):

    def set_email(self):
        self.safe_click(ForgotPasswordLocators.EMAIL_FIELD)
        self.find_element(ForgotPasswordLocators.EMAIL_FIELD).send_keys(random_email())

    def click_on_recover_button(self):
        self.safe_click(ForgotPasswordLocators.RECOVER_BUTTON)

    def wait_until_url_contains_forgot_password(self, timeout=10):
        self.wait_until(ec.url_contains(URL.FORGOT_PASS_URL), timeout)
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)