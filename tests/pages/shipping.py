from .base_page import BasePage
from .locators import ShippingPageLocators


class ShippingPage(BasePage):
    """Shipping page action methods come here."""

    def first_name(self, text):
        """sets first name"""
        self.driver.find_element(*ShippingPageLocators.FIRST_NAME).send_keys(text)

    def last_name(self, text):
        """sets last name"""
        self.driver.find_element(*ShippingPageLocators.LAST_NAME).send_keys(text)

    def company(self, text):
        """set company"""
        self.driver.find_element(*ShippingPageLocators.COMPANY).send_keys(text)

    def address(self, text):
        """set address"""
        self.driver.find_element(*ShippingPageLocators.ADDRESS).send_keys(text)

    def address_2(self, text):
        """set address_2"""
        self.driver.find_element(*ShippingPageLocators.ADDRESS_2).send_keys(text)

    def city(self, text):
        """set city"""
        self.driver.find_element(*ShippingPageLocators.CITY).send_keys(text)

    def state(self, value):
        """set state"""
        self.driver.find_element(*ShippingPageLocators.STATE).send_keys(value)

    def postal_code(self, text):
        """set postal_code"""
        self.driver.find_element(*ShippingPageLocators.POSTAL_CODE).send_keys(text)

    def country(self, value):
        """set country"""
        self.driver.find_element(*ShippingPageLocators.COUNTRY).send_keys(value)

    def shipping_method(self, value):
        """set shipping_method"""
        self.driver.find_element(*ShippingPageLocators.SHIPPING_METHOD).send_keys(value)

    def email(self, text):
        """set email"""
        self.driver.find_element(*ShippingPageLocators.EMAIL).send_keys(text)

    def int_phone(self, text):
        """set int_phone"""
        self.driver.find_element(*ShippingPageLocators.INT_PHONE).send_keys(text)

    def click_continue(self):
        self.driver.find_element(*ShippingPageLocators.CONTINUE_BUTTON).click()
