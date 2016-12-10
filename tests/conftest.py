import pytest
from selenium import webdriver

'''Stolen from https://jonathan.stoppani.name/posts/combining-pytest-and-selenium.html
# TODO: update for standalone selenium'''

@pytest.yield_fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()