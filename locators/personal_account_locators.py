from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    LOGOUT_BUTTON = (By.XPATH, './/button[contains(text(), "Выход")]')
    ORDER_HISTORY_BUTTON = (By.XPATH, './/a[contains(text(), "История заказов")]')
    LATEST_MADE_ORDER_ID = (By.XPATH, './/ul[contains(@class,"OrderHistory_profileList")]/li[last()]/a/div/p[contains(@class,"text text_type_digits-default")]')