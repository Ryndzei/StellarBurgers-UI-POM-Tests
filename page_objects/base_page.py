import time
from selenium.common import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators
from urls import URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def open(self, url):
        self.driver.get(url)

    def wait_until(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    def get_current_url(self):
        return self.driver.current_url

    def wait_until_all_elements_invisible(self, locator, timeout=15):
        def all_elements_invisible(driver):
            try:
                elements = driver.find_elements(*locator)
                return all(not element.is_displayed() for element in elements)
            except StaleElementReferenceException:
                return False

        return self.wait_until(all_elements_invisible, timeout=timeout)

    def click_personal_account(self):
        self.safe_click(BasePageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor(self):
        self.safe_click(BasePageLocators.CONSTRUCTOR_LINK)

    def click_orders_list(self):
        self.safe_click(BasePageLocators.ORDERS_LIST_LINK)

    def wait_until_url_to_be_base_page(self, timeout=15):
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)
        self.wait_until(ec.url_to_be(URL.BASE_URL), timeout)

    def wait_until_url_to_be_orders_list_page(self, timeout=15):
        self.wait_until_all_elements_invisible(BasePageLocators.OVERLAYS)
        self.wait_until(ec.url_to_be(URL.ORDERS_LIST_URL), timeout)

    def safe_click(self, locator, max_attempts=3, timeout=15, ignore_overlays=False):
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
                    print(f"Element found but not visible. Attempt {attempts + 1}/{max_attempts}")
            except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                print(f"Click intercepted. Attempt {attempts + 1}/{max_attempts}: {str(e)}")

            attempts += 1
            time.sleep(1)

        try:
            element = self.wait_until(ec.presence_of_element_located(locator), timeout=timeout)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
            return True
        except Exception as e:
            raise Exception(f"Final click attempt failed: {str(e)}")