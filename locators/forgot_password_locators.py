from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_FIELD = (By.XPATH, './/input[@name="name" and contains(@class, "input__textfield")]')
    RECOVER_BUTTON = (By.XPATH, './/button[contains(@class, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")]')
