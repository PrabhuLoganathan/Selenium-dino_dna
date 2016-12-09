from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseTestCase(object):

    def setup(self):
        self.driver = webdriver.Chrome()
        # TODO: implement standalone Selenium server
        # self.driver = webdriver.Remote(
        #     command_executor='http://localhost:4444/wd/hub',
        #     desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # TODO: review quit on every test after more tests are included
        self.driver.quit()
