from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ResetPasswordPageLocators(BasePage):
    PASS_ACTIVE_FIELD = (By.XPATH, './/fieldset[1]/div/div/input[@type="text"]')
    SHOW_PASS_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
