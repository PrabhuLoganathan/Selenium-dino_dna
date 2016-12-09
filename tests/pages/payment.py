from base_page import BasePage
from locators import PaymentPageLocators


class PaymentPage(BasePage):
    """Payment page action methods come here."""

    def credit_card_number(self, text):
        """sets cc number"""
        self.driver.find_element(*PaymentPageLocators.CREDIT_CARD_NUMBER).send_keys(text)

    def expiration(self, text):
        """sets expiration"""
        self.driver.find_element(*PaymentPageLocators.EXPIRATION).send_keys(text)

    def cvv(self, text):
        """set cvv"""
        self.driver.find_element(*PaymentPageLocators.CVV).send_keys(text)

    def click_continue(self):
        self.driver.find_element(*PaymentPageLocators.CONTINUE_BUTTON).click()
