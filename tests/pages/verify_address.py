from base_page import BasePage
from locators import VerifyAddressPageLocators


class VerifyAddressPage(BasePage):
    """VerifyAddress page action methods come here."""

    def verify_address_success(self):
        """verification summary includes success message"""
        success_message = 'We verified your shipping address and found an exact match.'

        summary = self.driver.find_element(*VerifyAddressPageLocators.VERIFICATION_SUMMARY).text
        if success_message not in summary:
            return False

        return True

    def click_continue(self):
        """clicks the continue button"""
        # TODO: button naming needs to be more concise, with 3 similar buttons on page
        self.driver.find_element(*VerifyAddressPageLocators.CONTINUE_BUTTON).click()
