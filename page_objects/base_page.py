import logging
import allure
from selenium.common import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators
from urls import URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти один элемент на странице по локатору")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти все элементы на странице по локатору")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Открыть страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидать условие")
    def wait_until(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ждать, пока все оверлеи исчезнут")
    def wait_until_all_elements_invisible(self, locator, timeout=15):
        def all_elements_invisible(driver):
            try:
                elements = driver.find_elements(*locator)
                return all(not element.is_displayed() for element in elements)
            except StaleElementReferenceException:
                return False

        return self.wait_until(all_elements_invisible, timeout=timeout)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_personal_account(self):
        self.safe_click(BasePageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик по ссылке 'Конструктор'")
    def click_constructor(self):
        self.safe_click(BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step("Клик по ссылке 'Лента заказов'")
    def click_orders_list(self):
        self.safe_click(BasePageLocators.ORDERS_LIST_LINK)

    @allure.step("Ожидать перехода на главную страницу")
    def wait_until_url_to_be_base_page(self, timeout=15):
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)
        self.wait_until(ec.url_to_be(URL.BASE_URL), timeout)

    @allure.step("Ожидать перехода на главную страницу")
    def wait_until_url_to_be_orders_list_page(self, timeout=15):
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)
        self.wait_until(ec.url_to_be(URL.ORDERS_LIST_URL), timeout)

    @allure.step("Клик по элементу")
    def safe_click(self, locator, max_attempts=3, timeout=15, ignore_overlays=False):
        logger = logging.getLogger(__name__)
        attempts = 0
        while attempts < max_attempts:
            try:
                if not ignore_overlays:
                    self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS, timeout=timeout)

                element = self.wait_until(ec.element_to_be_clickable(locator), timeout=timeout)

                if element.is_displayed():
                    element.click()
                    return True
                else:
                    logger.warning(f"Element found but not visible. Attempt {attempts + 1}/{max_attempts}")
            except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                logger.info(f"Click intercepted. Attempt {attempts + 1}/{max_attempts}: {str(e)}")

            attempts += 1

        try:
            element = self.wait_until(ec.presence_of_element_located(locator), timeout=timeout)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
            return True
        except Exception as e:
            raise Exception(f"Final click attempt failed: {str(e)}")