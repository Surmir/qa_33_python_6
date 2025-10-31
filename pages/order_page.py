from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators as BPLocs
from locators.order_page_locators import OrderPageLocators as OPLocs
from data import ColorScooter
import allure


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки страницы оформления "Для кого самокат"')
    def wait_load_order_form_one(self):
        self.wait_for_visibility_element(OPLocs.ORDER_HEADER_ONE)

    @allure.step('Нажимаем на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click_on_element(BPLocs.HEADER_LOGO_SCOOTER)

    @allure.step('Заполняем поле "Имя"')
    def set_name_placeholder(self, name):
        self.set_data(OPLocs.PLACEHOLDER_NAME, name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_last_name_placeholder(self, last_name):
        self.set_data(OPLocs.PLACEHOLDER_LAST_NAME, last_name)

    @allure.step('Заполняем поле "Адрес: куда привезти заказ"')
    def set_adress_placeholder(self, adress):
        self.set_data(OPLocs.PLACEHOLDER_ADRESS, adress)

    @allure.step('Заполняем поле "Станция метро"')
    def set_metro_station_placeholder(self, metro):
        element = OPLocs.PLACEHOLDER_METRO_STATION
        self.set_data(element, metro)
        self.select_text(element, metro)

    @allure.step('Заполняем поле "Телефон: на него позвонит курьер"')
    def set_phone_number_placeholder(self, phone):
        self.set_data(OPLocs.PLACEHOLDER_PHONE_NUMBER, phone)

    @allure.step('Нажимаем кнопку "Далее"')
    def click_button_next(self):
        self.click_on_element(OPLocs.BUTTON_NEXT)

    @allure.step('Заполнение полей в форме "Для кого самокат"')
    def set_one_form(self, name, last_name, adress, metro, phone):
        self.set_name_placeholder(name)
        self.set_last_name_placeholder(last_name)
        self.set_adress_placeholder(adress)
        self.set_metro_station_placeholder(metro)
        self.set_phone_number_placeholder(phone)

    @allure.step('Ожидание загрузки страницы оформления "Про аренду"')
    def wait_load_order_form_two(self):
        self.wait_for_visibility_element(OPLocs.ORDER_HEADER_TWO)

    @allure.step('Заполняем поле "Когда привезти самокат"')
    def set_date_placeholder(self, date):
        self.set_data(OPLocs.PLACEHOLDER_DATE, date)

    @allure.step('Заполняем поле "Срок аренды"')
    def set_rent_time_placeholder(self, rent_time):
        element = OPLocs.RENT_TIME
        self.click_on_element(element)
        self.select_text(element, rent_time)

    allure.step('Выбираем {color} цвет самоката')
    def choose_color_scooter(self, color):
        black = ColorScooter.COLOR_BLACK
        grey = ColorScooter.COLOR_GREY
        if color == black:
            self.click_on_element(OPLocs.CHECKBOX_BLACK)
        elif color == grey:
            self.click_on_element(OPLocs.CHECKBOX_GREY)
        else:
            print(f'Для выбора доступны следующие цвета({black}, {grey})')

    allure.step('Заполняем поле комментарий')
    def set_comment_placeholder(self, comment):
        self.set_data(OPLocs.PLACEHOLDER_COMMENT, comment)

    @allure.step('Нажимаем кнопку "Заказать" в низу формы оформления')
    def click_button_middle_order(self):
        self.click_on_element(OPLocs.MIDDLE_BUTTON_ORDER)

    @allure.step('Заполнение полей в форме "Про аренду"')
    def set_two_form(self, date, rent_time, color, comment):
        self.set_date_placeholder(date)
        self.set_rent_time_placeholder(rent_time)
        self.choose_color_scooter(color)
        self.set_comment_placeholder(comment)

    @allure.step('Ожидание загрузки формы подтверждения "Хотите оформить заказ?"')
    def wait_load_confirm_form(self):
        self.wait_for_visibility_element(OPLocs.ORDER_HEADER_CONFIRM)

    @allure.step('Нажимаем кнопку "Да"')
    def click_button_yes(self):
        self.click_on_element(OPLocs.BUTTON_YES)

    @allure.step('Проверка успешного оформления заказа')
    def check_success_order(self):
        assert self.wait_for_visibility_element(OPLocs.ORDER_HEADER_SUCCESS).is_displayed()
