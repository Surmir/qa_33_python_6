from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import UserOne, UserTwo
import pytest
import allure


class TestOrderPage():

    @allure.title('Проверка перехода на главную страницу по логотипу "Самокат"')
    @allure.description('При нажатии на логотип "Самокат", попадёшь на главную страницу «Самоката»')
    def test_scooter_logo_transition_to_main_page(self, driver):
        o_page = OrderPage(driver)
        m_page = MainPage(driver)

        o_page.open_order_page()
        o_page.wait_load_order_form_one()
        o_page.click_scooter_logo()
        m_page.wait_load_main_page()

        assert o_page.check_open_main_page() == True

    @allure.title('Проверка позитивного сценария "Заказ самоката" с двумя наборами данных')
    @allure.description('Заполняем форму заказа. ' \
    'Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа.')
    @pytest.mark.parametrize('user', [UserOne.USER_ONE, UserTwo.USER_TWO])
    def test_success_order_scooter(self, driver, user):
        o_page = OrderPage(driver)

        o_page.open_order_page()
        o_page.wait_load_order_form_one()
        o_page.set_one_form(user[0], user[1], user[2], user[3], user[4])
        o_page.click_button_next()

        o_page.wait_load_order_form_two()
        o_page.set_two_form(user[5], user[6], user[7], user[8])
        o_page.click_button_middle_order()
        o_page.wait_load_confirm_form()
        o_page.click_button_yes()

        assert o_page.check_success_order() == True
