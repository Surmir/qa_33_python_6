from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        self.driver.get(url)

    def check_page_url(self, url):
        actually_url = self.driver.current_url
        expected_url = url
        assert actually_url == expected_url

    def wait_for_visibility_element(self, element, wait_time=5):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(element))

    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    def skroll_to_element(self, element):
        element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_text(self, element, text):
        actually_url = self.driver.find_element(*element).text
        expected_url = text
        assert actually_url == expected_url

    def set_data(self, placeholder, data):
        self.driver.find_element(*placeholder).send_keys(data)
