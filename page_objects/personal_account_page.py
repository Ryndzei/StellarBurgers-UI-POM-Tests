from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators
from locators.personal_account_locators import PersonalAccountLocators
from page_objects.base_page import BasePage
from urls import URL


class PersonalAccountPage(BasePage):

    def wait_until_url_to_be_personal_account_page(self, timeout=15):
        self.wait_until(ec.url_to_be(URL.PERSONAL_ACCOUNT_URL), timeout)
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)

    def click_order_history_button(self):
        self.safe_click(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    def wait_until_url_to_be_personal_account_order_history_page(self, timeout=15):
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)
        self.wait_until(ec.url_to_be(URL.ORDER_HISTORY_URL), timeout)

    def click_logout_button(self):
        self.safe_click(PersonalAccountLocators.LOGOUT_BUTTON)

    def get_order_id_in_history(self, timeout=5):
        order_id_elem = self.wait_until(ec.visibility_of_element_located(PersonalAccountLocators.LATEST_MADE_ORDER_ID), timeout)
        return order_id_elem.text

