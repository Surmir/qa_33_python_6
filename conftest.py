import pytest
from selenium import webdriver
from urls import Url


#запуск браузера
@pytest.fixture
def driver():
    driver = webdriver.Firefox()

    yield driver

    driver.quit()

#запуск браузера с переходом на главную страницу сайта(для множества тестов без закрытия страницы)
@pytest.fixture(scope='class')
def driver_main_page():
    driver = webdriver.Firefox()
    driver.get(Url.MAIN_PAGE)

    yield driver

    driver.quit()
