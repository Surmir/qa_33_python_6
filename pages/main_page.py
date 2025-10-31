from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators as BPLocs
from locators.main_page_locators import MainPageLocators as MPLocs
from urls import Url
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.go_to_page(Url.MAIN_PAGE)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_load_main_page(self):
        self.wait_for_visibility_element(MPLocs.MAIN_HEADER)

    @allure.step('Нажимаем на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click_on_element(BPLocs.HEADER_LOGO_YANDEX)

    @allure.step('Проверяем переход на страницу "Дзен"')
    def check_open_page_dzen(self):
        actual_url = self.get_page_url()
        expect_url = Url.DZEN_PAGE
        assert actual_url == expect_url

    @allure.step('Нажимаем на кнопку "Заказать" в заголовке')
    def click_button_order_header(self):
        self.click_on_element(BPLocs.HEADER_BUTTON_ORDER)

    @allure.step('Нажимаем на кнопку "Заказать" в центре страницы')
    def click_button_order_middle(self):
        button = MPLocs.MIDDLE_BUTTON_ORDER
        self.skroll_to_element(button)
        self.click_on_element(button)

    @allure.step('Нажимаем на вопрос№{key} из раздела "Вопросы о важном"')
    def click_on_question(self, key):
        qestion = MPLocs.DICTIONARY_QUESTIONS[key]
        self.skroll_to_element(qestion)
        self.click_on_element(qestion)

    @allure.step('Ожидание появления ответа на вопрос №{key}')
    def wait_visibility_answer(self, key):
        self.wait_for_visibility_element(MPLocs.DICTIONARY_ANSWERS[key], 3)

    @allure.step('Получаем текст ответа на вопрос№{key}')
    def get_text_answer(self, key):
        self.get_text(MPLocs.DICTIONARY_ANSWERS[key])
