from base_page import BasePage
from locators import VerifyAddressPageLocators


class VerifyAddressPage(BasePage):
    """VerifyAddress page action methods come here."""

    def verify_text_success(self):
        """verification summary includes success message"""
        self.driver.find_element(*VerifyAddressPageLocators.VERIFICATION_SUMMARY)

    def click_continue(self):
        """clicks the continue button"""
        #TODO: button naming needs to be more concise, with 3 similar buttons on page
        self.driver.find_element(*VerifyAddressPageLocators.CONTINUE_BUTTON).click()
