from selenium.webdriver.common.by import By


class LoginAccountLocators:
    LOGIN_EMAIL_INPUT = (By.XPATH, './/fieldset[1]/div/div/input[@name="name"]')
    LOGIN_PASSWORD_INPUT = (By.XPATH, './/fieldset[2]/div/div/input[@name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, './/div[1]/div/main/div/div/p[2]/a[text()="Восстановить пароль"]')



