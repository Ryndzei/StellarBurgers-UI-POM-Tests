import allure
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.orders_list_page import OrdersListPage
from page_objects.personal_account_page import PersonalAccountPage
from urls import URL


@allure.feature("Лента заказов")
@allure.description("Этот класс содержит тесты для проверки функционала ленты заказов.")
class TestOrdersList:

    @allure.title("Открытие деталей заказа")
    @allure.description("Проверяет открытие всплывающего окна с деталями заказа при клике.")
    def test_details_of_order_pop_up_appear_on_click_successfully(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.open(URL.ORDERS_LIST_URL)
        orders_list_page.click_first_order()

        assert orders_list_page.is_order_details_text_displayed()
        assert orders_list_page.is_order_details_section_opened()

    @allure.title("Отображение заказов из истории")
    @allure.description("Проверяет отображение заказов из истории в ленте заказов.")
    def test_orders_from_history_are_in_orders_list(self, driver, user_create_and_cleanup):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        personal_account_page = PersonalAccountPage(driver)
        orders_list_page = OrdersListPage(driver)
        payload = user_create_and_cleanup
        login_page.open(URL.LOGIN_URL)
        login_page.set_email(payload["email"])
        login_page.set_password(payload["password"])
        login_page.click_login_button()
        login_page.wait_until_url_to_be_base_page()
        home_page.drag_and_drop_R2_D3_bun_to_constructor()
        home_page.click_order_button()
        order_id = "0" + home_page.get_order_id()
        home_page.click_close_pop_up_button()
        home_page.click_personal_account()
        personal_account_page.click_order_history_button()
        order_id_in_history = personal_account_page.get_order_id_in_history().lstrip('#')
        assert order_id == order_id_in_history
        personal_account_page.click_orders_list()
        order_id_in_orders_list = orders_list_page.get_last_order_id_in_orders_list()

        assert "#" + order_id_in_history in order_id_in_orders_list

    @allure.title("Увеличение счетчика 'За всё время'")
    @allure.description("Проверяет увеличение счетчика 'Выполнено за всё время' при новом заказе.")
    def test_all_time_orders_done_counter_amount_increase_successfully(self, driver, user_create_and_cleanup):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        orders_list_page = OrdersListPage(driver)
        orders_list_page.open(URL.ORDERS_LIST_URL)
        counter_amount_before_order = orders_list_page.get_all_time_orders_done_counter_amount()
        orders_list_page.click_personal_account()
        payload = user_create_and_cleanup
        login_page.set_email(payload["email"])
        login_page.set_password(payload["password"])
        login_page.click_login_button()
        login_page.wait_until_url_to_be_base_page()
        home_page.drag_and_drop_R2_D3_bun_to_constructor()
        home_page.click_order_button()
        home_page.click_close_pop_up_button()
        home_page.click_orders_list()
        counter_amount_after_order = orders_list_page.get_all_time_orders_done_counter_amount()
        orders_list_page.wait_until_all_time_orders_done_counter_increase(counter_amount_before_order)

        assert counter_amount_after_order > counter_amount_before_order

    @allure.title("Увеличение счетчика 'За сегодня'")
    @allure.description("Проверяет увеличение счетчика 'Выполнено за сегодня' при новом заказе.")
    def test_today_orders_done_counter_amount_increase_successfully(self, driver, user_create_and_cleanup):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        orders_list_page = OrdersListPage(driver)
        orders_list_page.open(URL.ORDERS_LIST_URL)
        counter_amount_before_order = orders_list_page.get_today_orders_done_counter_amount()
        orders_list_page.click_personal_account()
        payload = user_create_and_cleanup
        login_page.set_email(payload["email"])
        login_page.set_password(payload["password"])
        login_page.click_login_button()
        login_page.wait_until_url_to_be_base_page()
        home_page.drag_and_drop_R2_D3_bun_to_constructor()
        home_page.click_order_button()
        home_page.click_close_pop_up_button()
        home_page.click_orders_list()
        counter_amount_after_order = orders_list_page.get_today_orders_done_counter_amount()
        orders_list_page.wait_until_today_orders_done_counter_increase(counter_amount_before_order)

        assert counter_amount_after_order > counter_amount_before_order

    @allure.title("Отображение заказа в 'В работе'")
    @allure.description("Проверяет появление номера заказа в разделе 'В работе' после оформления.")
    def test_order_id_appears_in_orders_in_progress_section_successfully(self, driver, user_create_and_cleanup):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        orders_list_page = OrdersListPage(driver)
        login_page.open(URL.LOGIN_URL)
        payload = user_create_and_cleanup
        login_page.set_email(payload["email"])
        login_page.set_password(payload["password"])
        login_page.click_login_button()
        login_page.wait_until_url_to_be_base_page()
        login_page.wait_until_url_to_be_base_page()
        home_page.drag_and_drop_R2_D3_bun_to_constructor()
        home_page.click_order_button()
        order_id = "0" + home_page.get_order_id()
        home_page.click_close_pop_up_button()
        home_page.click_orders_list()
        orders_list_page.wait_until_order_id_appears_in_orders_in_progress_ids(order_id)
        orders_in_progress_ids = orders_list_page.get_orders_in_progress_ids()

        assert order_id in orders_in_progress_ids