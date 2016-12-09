from base_test_case import BaseTestCase
from pages.cart import CartPage
from pages.shipping import ShippingPage
from pages.verify_address import VerifyAddressPage
from pages.payment import PaymentPage


class TestCheckout(BaseTestCase):
    """A sample test class to show how page object works"""

    def setup(self):
        super(TestCheckout, self).setup()

        # 1) Visit store.23andme.com/en-us/
        self.driver.get('https://store.23andme.com/en-us/')

    def test_add_kit(self):
        """
        Tests cart add kit.
        """

        # 2) Add 5 kits and enters unique names for each kit
        cart_page = CartPage(self.driver)
        # TODO: assert on page

        cart_page.add_bundle('Trex')
        cart_page.add_bundle('Stegasaurus')
        cart_page.add_bundle('Jim')
        cart_page.add_bundle('Sam')
        cart_page.add_bundle('Manny')
        # TODO: add assertions for presence of bundles
        cart_page.click_continue()

        # 3) Continue to the shipping page and enter a valid US shipping address and other info.
        shipping_page = ShippingPage(self.driver)
        # TODO: assert on page

        shipping_page.first_name('Brian')
        shipping_page.last_name('Jameson')
        shipping_page.company('Jurrasic Park')
        shipping_page.address('3150 SE Division')
        shipping_page.address_2('412')
        shipping_page.city('Portland')
        shipping_page.state('OR')
        shipping_page.postal_code('97202')
        shipping_page.country('US')
        shipping_page.shipping_method('matrixrate_standard')
        shipping_page.email('dino@gmail.com')
        shipping_page.int_phone('4406660000')
        shipping_page.click_continue()

        # 4) Continue through the shipping verification page and verifies that the payment page is reached.
        verify_address_page = VerifyAddressPage(self.driver)
        # TODO: assert on page
        # TODO: add verifcation for text of valid address match
        verify_address_page.click_continue()

        payment_page = PaymentPage(self.driver)
        # TODO: add verification that payment page is reached


    def teardown(self):
        pass