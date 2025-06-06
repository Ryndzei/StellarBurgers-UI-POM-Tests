from selenium.webdriver.support import expected_conditions as ec
from locators.home_page_locators import HomePageLocators
from page_objects.base_page import BasePage


class HomePage(BasePage):

    def click_on_ingredient(self):
        self.safe_click(HomePageLocators.INGREDIENT_R2_D3_BUN)

    def wait_for_details_popup_appear(self, timeout=10):
        self.wait_until(ec.visibility_of_element_located(HomePageLocators.DETAILS_SECTION_OPENED_STATE), timeout)

    def is_details_text_displayed(self):
        return self.find_element(HomePageLocators.DETAILS_OF_INGREDIENT_TEXT).is_displayed()

    def is_details_section_opened(self):
        element = self.find_element(HomePageLocators.DETAILS_SECTION_OPENED_STATE)
        return "Modal_modal_opened__3ISw4" in element.get_attribute("class")

    def click_close_pop_up_button(self):
        self.safe_click(HomePageLocators.DETAILS_OF_INGREDIENT_CLOSE_BUTTON, ignore_overlays=True)

    def is_details_section_closed(self):
        element = self.find_element(HomePageLocators.DETAILS_SECTION_CLOSED_STATE)
        return "Modal_modal_opened__3ISw4" not in element.get_attribute("class")

    def click_order_button(self):
        self.safe_click(HomePageLocators.MAKE_AN_ORDER_BUTTON)

    def is_order_in_progress_text_displayed(self):
        return self.find_element(HomePageLocators.ORDER_IN_PROGRESS_TEXT).is_displayed()

    def drag_and_drop_R2_D3_bun_to_constructor(self):
        source = self.find_element(HomePageLocators.SOURCE_DROP)
        target = self.find_element(HomePageLocators.TARGET_DROP)

        # JavaScript для лучшей эмуляции dragstart-dragover-drop и стабильности теста в Firefox.
        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            const dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            source.dispatchEvent(dragStartEvent);

            const dragOverEvent = new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dragStartEvent.dataTransfer
            });
            target.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dragStartEvent.dataTransfer
            });
            target.dispatchEvent(dropEvent);
        """, source, target)

    def get_R2_D3_bun_ingredient_counter(self):
        counter_element = self.find_element(HomePageLocators.R2_D3_BUN_COUNTER)
        return int(counter_element.text) if counter_element.text else 0

    def get_order_id(self, timeout=5):
        order_id = self.wait_until(ec.visibility_of_element_located(HomePageLocators.ORDER_ID), timeout)
        self.wait_until(lambda driver: '2' in order_id.text, timeout)
        return order_id.text