from selenium.webdriver.common.by import By


class HomePageLocators:
    DETAILS_OF_INGREDIENT_TEXT = (By.XPATH, './/h2[contains(text(), "Детали ингредиента")]')
    DETAILS_SECTION_OPENED_STATE = (By.XPATH, './/section[1][@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]')
    DETAILS_SECTION_CLOSED_STATE = (By.XPATH, './/section[1][@class="Modal_modal__P3_V5"]')
    INGREDIENT_R2_D3_BUN = (By.XPATH, './/a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa6d")]')
    DETAILS_OF_INGREDIENT_CLOSE_BUTTON = (By.XPATH, './/section[1]/div[1]/button[contains(@class, "Modal_modal__close__TnseK")]')
    MAKE_AN_ORDER_BUTTON = (By.XPATH, './/button[contains(text(), "Оформить заказ")]')
    ORDER_IN_PROGRESS_TEXT = (By.XPATH, '//p[contains(text(), "Ваш заказ начали готовить")]')
    SOURCE_DROP = INGREDIENT_R2_D3_BUN
    TARGET_DROP = (By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket__list__l9dp_")]')
    R2_D3_BUN_COUNTER = (By.XPATH, './/section[1]/div[2]/ul[1]/a[1]/div/p[contains(@class, "counter_counter__num__3nue1")]')
    ORDER_ID = (By.XPATH, './/div[1]/div/h2')