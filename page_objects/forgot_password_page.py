import allure
from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators
from locators.forgot_password_locators import ForgotPasswordLocators
from page_objects.base_page import BasePage
from urls import URL


class ForgotPasswordPage(BasePage):

    @allure.step("Ввести email для восстановления пароля")
    def set_email(self, email):
        self.safe_click(ForgotPasswordLocators.EMAIL_FIELD)
        self.find_element(ForgotPasswordLocators.EMAIL_FIELD).send_keys(email)

    @allure.step("Нажать кнопку 'Восстановить'")
    def click_on_recover_button(self):
        self.safe_click(ForgotPasswordLocators.RECOVER_BUTTON)

    @allure.step("Ожидать перехода на страницу восстановления пароля")
    def wait_until_url_contains_forgot_password(self, timeout=10):
        self.wait_until(ec.url_contains(URL.FORGOT_PASS_URL), timeout)
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)