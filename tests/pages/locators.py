from selenium.webdriver.common.by import By


class CartPageLocators(object):
    """A class for cart page locators."""
    ADD_BUNDLE_BUTTON = (By.CSS_SELECTOR, 'span.quantity-control-button.js-add-kit')
    KIT_ITEM = (By.CSS_SELECTOR, 'div.js-kit-item.cart-item-row')
    # KIT_ITEM_SAVING = (By.CSS_SELECTOR, 'div.js-kit-item.cart-item-row.js-saving')
    ITEM_NAME = (By.CLASS_NAME, 'js-kit-name')
    ITEM_LABEL = (By.CLASS_NAME, 'item-kit-label')
    CONTINUE_BUTTON = (By.CLASS_NAME, 'submit')


class ShippingPageLocators(object):
    """A class for Shipping page locators. """
    FIRST_NAME = (By.ID, 'id_first_name')
    LAST_NAME = (By.ID, 'id_last_name')
    COMPANY = (By.ID, 'id_company')
    ADDRESS = (By.ID, 'id_address')
    ADDRESS_2 = (By.ID, 'id_address2')
    CITY = (By.ID, 'id_city')
    STATE = (By.ID, 'id_state')
    POSTAL_CODE = (By.ID, 'id_postal_code')
    COUNTRY = (By.ID, 'id_country')
    SHIPPING_METHOD = (By.ID, 'id_shipping_method')
    EMAIL = (By.ID, 'id_email')
    INT_PHONE = (By.ID, 'id_int_phone')
    CONTINUE_BUTTON = (By.CLASS_NAME, 'submit')


class VerifyAddressPageLocators(object):
    """A class for Verify Address page locators."""
    VERIFICATION_SUMMARY = (By.CLASS_NAME, 'verification-summary')
    CONTINUE_BUTTON = (By.CLASS_NAME, 'button-continue')


class PaymentPageLocators(object):
    """A class for Payment page locators."""
    CREDIT_CARD_NUMBER = (By.ID, 'credit-card-number')
    EXPIRATION = (By.ID, 'expiration')
    CVV = (By.ID, 'cvv')
    CONTINUE_BUTTON = (By.CLASS_NAME, 'submit')
