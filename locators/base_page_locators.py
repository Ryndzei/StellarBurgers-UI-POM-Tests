from selenium.webdriver.common.by import By


class BasePageLocators:
    OVERLAYS = (By.XPATH, './/div[contains(@class, "Modal_modal_overlay")]')
    CONSTRUCTOR_LINK = (By.XPATH, './/p[text()="Конструктор"]')
    ORDERS_LIST_LINK = (By.XPATH, './/p[text()="Лента Заказов"]')
    LOGO_LINK = (By.XPATH, './/nav/div/a[@href="/"]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')