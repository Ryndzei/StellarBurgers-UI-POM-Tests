import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from page_objects.base_page import BasePage
from urls import URL


class ResetPasswordPage(BasePage):

    @allure.step("Клик по иконке 'Показать пароль'")
    def click_on_show_password_field_button(self):
        self.safe_click(ResetPasswordPageLocators.SHOW_PASS_BUTTON)

    @allure.step("Ожидать активации поля ввода пароля")
    def wait_for_password_field_active(self, timeout=5):
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)
        self.wait_until(ec.visibility_of_element_located(ResetPasswordPageLocators.PASS_ACTIVE_FIELD), timeout=timeout)

    @allure.step("Проверить, что поле пароля активно")
    def is_password_field_active(self) -> bool:
        try:
            self.wait_until(ec.visibility_of_element_located(ResetPasswordPageLocators.PASS_ACTIVE_FIELD), timeout=5)
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидать перехода на страницу сброса пароля")
    def wait_until_url_contains_reset_password(self, timeout=10):
        self.wait_until(ec.url_contains(URL.RESET_PASS_URL), timeout)
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)