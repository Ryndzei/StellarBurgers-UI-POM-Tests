from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    LOGOUT_BUTTON = (By.XPATH, './/ul/li[3]/button[contains(text(), "Выход")]')
    ORDER_HISTORY_BUTTON = (By.XPATH, './/li[2]/a[contains(text(), "История заказов")]')
    LATEST_MADE_ORDER_ID = (By.XPATH, './/ul[contains(@class,"OrderHistory_profileList")]/li[last()]/a/div[1]/p[1][contains(@class,"text text_type_digits-default")]')