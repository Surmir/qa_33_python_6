from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Answers
import pytest
import allure


class TestMainPage():

    @allure.title('Проверка перехода в "Дзен" по логотипу "Яндекс"')
    @allure.description('При нажатии на логотип Яндекса, ' \
    'в новом окне через редирект откроется главная страница Дзена')
    def test_yandex_logo_transition_to_dzen(self, driver):
        m_page = MainPage(driver)

        m_page.open_main_page()
        m_page.wait_load_main_page()
        m_page.click_yandex_logo()
        m_page.wait_load_dzen_page()
        
        assert m_page.check_open_page_dzen()

    @allure.title('Проверка перехода на страницу заказа по кнопке "Заказать" в шапке страницы')
    def test_button_order_in_header(self, driver):
        m_page = MainPage(driver)
        o_page = OrderPage(driver)

        m_page.open_main_page()
        m_page.wait_load_main_page()
        m_page.click_button_order_header()
        o_page.wait_load_order_form_one()

        assert m_page.check_open_order_page()

    @allure.title('Проверка перехода на страницу заказа по кнопке "Заказать" в центре страницы')
    def test_button_order_in_middle(self, driver):
        m_page = MainPage(driver)
        o_page = OrderPage(driver)

        m_page.open_main_page()
        m_page.wait_load_main_page()
        m_page.click_button_order_middle()
        o_page.wait_load_order_form_one()

        assert m_page.check_open_order_page()

    @allure.title('Проверка выпадающий список в разделе «Вопросы о важном»')
    @allure.description('Нужно проверить: при нажатии на вопрос№{key}, открывается соответствующий текст')
    @pytest.mark.parametrize('key', [1, 2, 3, 4, 5, 6, 7, 8])
    def test_text_answer_correct(self, driver, key):
        m_page = MainPage(driver)
        expect_text = Answers.DICTIONARY_ANSWERS[key]

        m_page.open_main_page()
        m_page.wait_load_main_page()
        m_page.click_on_question(key)
        m_page.wait_visibility_answer(key)
        actual_text = m_page.get_text_answer(key)

        assert expect_text == actual_text
