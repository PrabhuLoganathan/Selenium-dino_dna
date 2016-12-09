from base_test_case import BaseTestCase
from pages.cart import CartPage
from pages.shipping import ShippingPage
from pages.verify_address import VerifyAddressPage
from pages.payment import PaymentPage


class TestCheckout(BaseTestCase):
    """A sample test class to show how page object works"""

    def setup(self):
        super(TestCheckout, self).setup()

    def test_checkout_many_kits(self):
        """
        Tests many kits can be added to cart.
        """

        # TODO: update url match timeout to be more realistic of requirements

        # 1) Visit store.23andme.com/en-us/
        cart_page = CartPage(self.driver, 'https://store.23andme.com/en-us/')
        cart_page.open()
        assert cart_page.url_matches('https://store.23andme.com/en-us/cart/', timeout=5), 'Cart page not reached'

        # 2) Add 5 kits and enters unique names for each kit
        cart_page.add_health_ancestory_kit('Trex')
        assert cart_page.cart_item_match(order=1, label='Health + Ancestry', name='Trex')

        cart_page.add_health_ancestory_kit('Stegasaurus')
        assert cart_page.cart_item_match(order=2, label='Health + Ancestry', name='Stegasaurus')

        cart_page.add_health_ancestory_kit('Jim')
        assert cart_page.cart_item_match(order=3, label='Health + Ancestry', name='Jim')

        cart_page.add_health_ancestory_kit('Sam')
        assert cart_page.cart_item_match(order=4, label='Health + Ancestry', name='Sam')

        cart_page.add_health_ancestory_kit('Manny')
        assert cart_page.cart_item_match(order=5, label='Health + Ancestry', name='Manny')

        cart_page.click_continue()

        # 3) Continue to the shipping page and enter a valid US shipping address and other info.
        shipping_page = ShippingPage(self.driver)
        assert shipping_page.url_matches('https://store.23andme.com/en-us/shipping/', timeout=10), \
            'Shipping page not reached'

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
        assert verify_address_page.url_matches('https://store.23andme.com/en-us/verifyaddress/', timeout=10), \
            'Verify Address page not reached'
        assert verify_address_page.verify_address_success(), 'Verify Address address no valid'
        verify_address_page.click_continue()

        payment_page = PaymentPage(self.driver)
        assert payment_page.url_matches('https://store.23andme.com/en-us/payment/', timeout=10), \
            'Payment page not reached'
