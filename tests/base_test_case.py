from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseTestCase(object):
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Chrome()
        # TODO: implement standalone Selenium server
        # self.driver = webdriver.Remote(
        #     command_executor='http://localhost:4444/wd/hub',
        #     desired_capabilities=DesiredCapabilities.CHROME)

    def setup(self):
        pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    @classmethod
    def teardown_class(self):
        pass