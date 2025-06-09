from selenium.webdriver.common.by import By


class LoginAccountLocators:
    LOGIN_EMAIL_INPUT = (By.XPATH, './/input[@name="name"]')
    LOGIN_PASSWORD_INPUT = (By.XPATH, './/input[@name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, './/a[text()="Восстановить пароль"]')



