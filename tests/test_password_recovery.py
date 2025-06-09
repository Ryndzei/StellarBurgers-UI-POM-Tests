import allure
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.login_page import LoginPage
from page_objects.reset_password_page import ResetPasswordPage
from random_data import random_email
from urls import URL


class TestPasswordRecovery:

    @allure.feature("Восстановление пароля")
    @allure.description("Этот класс содержит тесты для проверки функционала восстановления пароля.")
    def test_go_to_forgot_password_page_successfully(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        login_page.open(URL.LOGIN_URL)
        login_page.click_forgot_password_button()
        forgot_password_page.wait_until_url_contains_forgot_password()

        assert URL.FORGOT_PASS_URL == forgot_password_page.get_current_url()

    @allure.title("Переход на страницу сброса пароля")
    @allure.description("Проверяет переход на страницу сброса пароля после ввода email.")
    def test_go_to_reset_password_page_successfully(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page.open(URL.FORGOT_PASS_URL)
        forgot_password_page.set_email(random_email())
        forgot_password_page.click_on_recover_button()
        reset_password_page.wait_until_url_contains_reset_password()

        assert URL.RESET_PASS_URL == reset_password_page.get_current_url()

    @allure.title("Активация поля пароля")
    @allure.description("Проверяет активацию поля пароля на странице сброса.")
    def test_make_field_active_on_reset_password_page_successfully(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page.open(URL.FORGOT_PASS_URL)
        forgot_password_page.set_email(random_email())
        forgot_password_page.click_on_recover_button()
        reset_password_page.click_on_show_password_field_button()

        assert reset_password_page.is_password_field_active()