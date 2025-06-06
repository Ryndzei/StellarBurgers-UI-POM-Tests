import allure
from urls import URL


@allure.feature("Основной функционал")
@allure.description("Этот класс содержит тесты для проверки основного функционала приложения.")
class TestBasicFunctionality:

    @allure.title("Переход на страницу 'Конструктор'")
    @allure.description("Проверяет успешный переход на главную страницу при клике на 'Конструктор'.")
    def test_go_to_constructor_page_successfully(self, home_page, login_page):
        login_page.open(URL.LOGIN_URL)
        login_page.click_constructor()
        login_page.wait_until_url_to_be_base_page()

        assert URL.BASE_URL == home_page.get_current_url()

    @allure.title("Переход на страницу 'Лента заказов'")
    @allure.description("Проверяет переход на страницу ленты заказов при клике на соответствующую ссылку.")
    def test_go_to_orders_list_page_successfully(self, home_page, orders_list_page):
        home_page.open(URL.BASE_URL)
        home_page.click_orders_list()
        home_page.wait_until_url_to_be_orders_list_page()

        assert URL.ORDERS_LIST_URL == orders_list_page.get_current_url()

    @allure.title("Открытие деталей ингредиента")
    @allure.description("Проверяет открытие всплывающего окна с деталями ингредиента при клике.")
    def test_details_of_ingredient_pop_up_appear_on_click_successfully(self, home_page):
        home_page.open(URL.BASE_URL)
        home_page.click_on_ingredient()
        home_page.wait_for_details_popup_appear()

        assert home_page.is_details_text_displayed()
        assert home_page.is_details_section_opened()

    @allure.title("Закрытие деталей ингредиента")
    @allure.description("Проверяет закрытие всплывающего окна с деталями ингредиента.")
    def test_close_details_of_ingredient_pop_up_on_click_button_successfully(self, home_page):
        home_page.open(URL.BASE_URL)
        home_page.click_on_ingredient()
        home_page.wait_for_details_popup_appear()
        home_page.click_close_pop_up_button()

        assert home_page.is_details_section_closed()

    @allure.title("Увеличение счетчика ингредиента")
    @allure.description("Проверяет увеличение счетчика при добавлении ингредиента в заказ.")
    def test_counter_of_ingredient_increases_successfully(self, home_page):
        home_page.open(URL.BASE_URL)
        initial_counter = home_page.get_R2_D3_bun_ingredient_counter()
        home_page.drag_and_drop_R2_D3_bun_to_constructor()
        updated_counter = home_page.get_R2_D3_bun_ingredient_counter()

        assert updated_counter == initial_counter + 2

    @allure.title("Оформление заказа")
    @allure.description("Проверяет успешное оформление заказа залогиненным пользователем.")
    def test_make_an_order_when_logged_in_successfully(self, login_page, home_page, user_create_and_cleanup):
        payload = user_create_and_cleanup
        login_page.open(URL.LOGIN_URL)
        login_page.set_email(payload["email"])
        login_page.set_password(payload["password"])
        login_page.click_login_button()
        login_page.wait_until_url_to_be_base_page()
        home_page.click_order_button()

        assert home_page.is_order_in_progress_text_displayed()

