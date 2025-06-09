from selenium.webdriver.common.by import By


class OrdersListLocators:

    FIRST_ORDER_IN_ORDERS_LIST = (By.XPATH, '//main/div/div/ul/li[1]')
    ORDER_DETAILS_SECTION_CLOSED_STATE = (By.XPATH, './/section[2][@class="Modal_modal__P3_V5"]')
    ORDER_DETAILS_SECTION_OPENED_STATE = (By.XPATH, './/section[2][@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]')
    FIRST_ORDER_DETAILS_SECTION_TEXT = (By.XPATH, './/p[contains(text(), "Cостав")]')
    LAST_MADE_ORDER_ID = (By.XPATH, './/li[1]/a/div[1]/p[1][@class="text text_type_digits-default"]')
    ALL_TIME_ORDERS_DONE_COUNTER = (By.XPATH, './/div[2]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    TODAY_ORDERS_DONE_COUNTER = (By.XPATH, './/div[3]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    ORDERS_IN_PROGRESS_IDS = (By.XPATH, './/div[1]/ul[2]/li')