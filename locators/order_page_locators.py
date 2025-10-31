from selenium.webdriver.common.by import By


class OrderPageLocators():
    #лист оформления №1
    #заголовок страницы
    ORDER_HEADER_1 = (By.XPATH, ".//div[text()='Для кого самокат']")
    #поля заполнения
    PLACEHOLDER_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    PLACEHOLDER_LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    PLACEHOLDER_ADRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    PLACEHOLDER_METRO_STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PLACEHOLDER_PHONE_NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    #кнопка далее
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Далее']")
    #лист оформления №2
    #заголовок страницы
    ORDER_HEADER_2 = (By.XPATH, ".//div[text()='Про аренду']")
    #поля заполнения
    PLACEHOLDER_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME = (By.XPATH, ".//div[text()='* Срок аренды']")
    COLOR_SCOOTER = (By.XPATH, ".//div[text()='Цвет самоката']")
    CHECKBOX_BLACK = (By.ID, "black")
    CHECKBOX_GREY = (By.ID, "grey")
    PLACEHOLDER_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    MIDDLE_BUTTON_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    #лист подтверждения заказа
    ORDER_HEADER_3 = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, ".//button[text()='Да']")
    #лист успешног оформления
    ORDER_HEADER_SUCCESS = (By.XPATH, ".//div[text()='Заказ оформлен']")
