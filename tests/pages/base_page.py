from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException


class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    See current documentation on http://selenium-python.readthedocs.io/page-objects.html
    TODO: replace with Webium or other existing page object package
    """

    def __init__(self, driver, url=None):
        if url:
            self.url = url
        self.driver = driver

    def open(self):
        if not self.url:
            raise Exception("Must set url to open page")
        self.driver.get(self.url)

    def url_matches(self, url_match, timeout=5):
        # TODO: update this verify against class's defined url
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(
                lambda u: self.driver.current_url == url_match
            )
            return True
        except TimeoutException:
            return False
