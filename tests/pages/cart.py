from base_page import BasePage
from locators import CartPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    """Cart page action methods come here."""

    def add_health_ancestory_kit(self, name):
        """adds new bundle kit with name"""

        item_count = len(self.driver.find_elements(*CartPageLocators.KIT_ITEM))

        add_button = self.driver.find_element(*CartPageLocators.ADD_BUNDLE_BUTTON)
        add_button.click()

        # wait for new item to be in list
        WebDriverWait(self.driver, 5).until(
            lambda b: len(self.driver.find_elements(*CartPageLocators.KIT_ITEM)) == item_count + 1
        )

        # select last item added
        item = self.driver.find_elements(*CartPageLocators.KIT_ITEM)[-1]

        # update the item name
        item_name = item.find_element(*CartPageLocators.ITEM_NAME)
        item_name.send_keys(name)

        # wait for name to save
        # TODO: locator not passable to expected condition in lambda
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.js-kit-item.cart-item-row.js-saving'))
        )

        # wait for save complete
        # TODO: locator not passable to expected condition in lambda
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div.js-kit-item.cart-item-row.js-saving'))
        )

    def click_continue(self):
        """clicks Continue button"""

        # click the continue button
        button = self.driver.find_element(*CartPageLocators.CONTINUE_BUTTON)
        button.click()

    def cart_item_match(self, order, label, name=None):
        # TODO: improve failure messaging for order/label/name
        # get all items
        items = self.driver.find_elements(*CartPageLocators.KIT_ITEM)

        # verify order in list
        order_index = order - 1
        try:
            items[order_index]
        except IndexError:
            return False

        # verify label text matches
        actual_label = items[order_index].find_element(*CartPageLocators.ITEM_LABEL).text
        if not label == actual_label:
            return False

        # verify name on item
        if name:
            actual_name = items[order_index].find_element(*CartPageLocators.ITEM_NAME).get_attribute('value')
            if not name == actual_name:
                return False

        return True
