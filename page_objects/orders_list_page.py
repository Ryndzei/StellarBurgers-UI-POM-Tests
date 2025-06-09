import allure
from selenium.webdriver.support import expected_conditions as ec
from locators.orders_list_locators import OrdersListLocators
from page_objects.base_page import BasePage


class OrdersListPage(BasePage):

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order(self):
        self.safe_click(OrdersListLocators.FIRST_ORDER_IN_ORDERS_LIST)

    @allure.step("Проверить, что окно деталей заказа открыто")
    def is_order_details_section_opened(self):
        element = self.find_element(OrdersListLocators.ORDER_DETAILS_SECTION_OPENED_STATE)
        return "Modal_modal_opened__3ISw4" in element.get_attribute("class")

    @allure.step("Проверить отображение текста с деталями заказа")
    def is_order_details_text_displayed(self):
        return self.find_element(OrdersListLocators.FIRST_ORDER_DETAILS_SECTION_TEXT).is_displayed()

    @allure.step("Получить ID последнего заказа в ленте")
    def get_last_order_id_in_orders_list(self, timeout=5):
        order_id = self.wait_until(ec.visibility_of_element_located(OrdersListLocators.LAST_MADE_ORDER_ID), timeout)
        return order_id.text

    @allure.step("Получить текущее значение счётчика 'Выполнено за всё время'")
    def get_all_time_orders_done_counter_amount(self, timeout=5):
        amount = self.wait_until(ec.visibility_of_element_located(OrdersListLocators.ALL_TIME_ORDERS_DONE_COUNTER), timeout)
        return int(amount.text)

    @allure.step("Получить текущее значение счётчика 'Выполнено сегодня'")
    def get_today_orders_done_counter_amount(self, timeout=5):
        amount = self.wait_until(ec.visibility_of_element_located(OrdersListLocators.TODAY_ORDERS_DONE_COUNTER), timeout)
        return int(amount.text)

    @allure.step("Дождаться увеличения счётчика 'Выполнено за всё время'")
    def wait_until_all_time_orders_done_counter_increase(self, initial_value, timeout=5):
        self.wait_until(lambda driver: int(self.get_all_time_orders_done_counter_amount()) > initial_value, timeout)

    @allure.step("Дождаться увеличения счётчика 'Выполнено сегодня'")
    def wait_until_today_orders_done_counter_increase(self, initial_value, timeout=5):
        self.wait_until(lambda driver: int(self.get_today_orders_done_counter_amount()) > initial_value, timeout)

    @allure.step("Получить список ID заказов в разделе 'В работе'")
    def get_orders_in_progress_ids(self):
        elements = self.find_elements(OrdersListLocators.ORDERS_IN_PROGRESS_IDS)
        return [el.text.strip() for el in elements]

    @allure.step("Дождаться появления заказа в разделе 'В работе'")
    def wait_until_order_id_appears_in_orders_in_progress_ids(self, order_id):
        self.wait_until(lambda driver: order_id in self.get_orders_in_progress_ids())


