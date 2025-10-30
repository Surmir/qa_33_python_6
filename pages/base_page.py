from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу {url}')
    def go_to_page(self, url):
        self.driver.get(url)

    @allure.step('Проверяем URL({url}) страницы')
    def check_page_url(self, url):
        actually_url = self.driver.current_url
        expected_url = url
        assert actually_url == expected_url, f"Url({actually_url}) не совпадает с ({expected_url})"
    
    @allure.step('Ожидаем видимости элемента страницы')
    def wait_for_visibility_element(self, element, wait_time=5):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(element))

    @allure.step('Нажимаем на элемент страницы')
    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step('Прокручиваем до элемента страницы')
    def skroll_to_element(self, element):
        element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Проверяем текст({text})')
    def check_text(self, element, text):
        actually_text = self.driver.find_element(*element).text
        expected_text = text
        assert actually_text == expected_text, f"Текст({actually_text}) не совпадает с ({expected_text})"

    @allure.step('Заполняем поле({placeholder})')
    def set_data(self, placeholder, data):
        self.driver.find_element(*placeholder).send_keys(data)
