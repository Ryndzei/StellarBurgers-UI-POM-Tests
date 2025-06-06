import allure
from urls import URL


@allure.feature("Личный кабинет")
@allure.description("Этот класс содержит тесты для проверки функционала личного кабинета.")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет")
    @allure.description("Проверяет успешный переход в личный кабинет залогиненным пользователем.")
    def test_go_to_personal_account_page_successfully(self, login_page, personal_account_page, home_page, user_create_and_cleanup):
        payload = user_create_and_cleanup
        login_page.open(URL.LOGIN_URL)
        login_page.set_email(payload["email"])
        login_page.set_password(payload["password"])
        login_page.click_login_button()
        login_page.wait_until_url_to_be_base_page()
        home_page.click_personal_account()
        personal_account_page.wait_until_url_to_be_personal_account_page()

        assert URL.PERSONAL_ACCOUNT_URL == personal_account_page.get_current_url()

    @allure.title("Переход в историю заказов")
    @allure.description("Проверяет переход в раздел 'История заказов' из личного кабинета.")
    def test_go_to_personal_account_order_history_successfully(self, login_page, personal_account_page, home_page, user_create_and_cleanup):
        payload = user_create_and_cleanup
        login_page.open(URL.LOGIN_URL)
        login_page.set_email(payload["email"])
        login_page.set_password(payload["password"])
        login_page.click_login_button()
        login_page.wait_until_url_to_be_base_page()
        home_page.click_personal_account()
        personal_account_page.wait_until_url_to_be_personal_account_page()
        personal_account_page.click_order_history_button()
        personal_account_page.wait_until_url_to_be_personal_account_order_history_page()

        assert URL.ORDER_HISTORY_URL == personal_account_page.get_current_url()

    @allure.title("Выход из аккаунта")
    @allure.description("Проверяет успешный выход из аккаунта через личный кабинет.")
    def test_logout_from_personal_account_successfully(self, login_page, personal_account_page, home_page, user_create_and_cleanup):
        payload = user_create_and_cleanup
        login_page.open(URL.LOGIN_URL)
        login_page.set_email(payload["email"])
        login_page.set_password(payload["password"])
        login_page.click_login_button()
        login_page.wait_until_url_to_be_base_page()
        home_page.click_personal_account()
        personal_account_page.wait_until_url_to_be_personal_account_page()
        personal_account_page.click_logout_button()
        login_page.wait_until_url_to_be_login_page()

        assert URL.LOGIN_URL == login_page.get_current_url()