from selenium.webdriver.common.by import By


class OrderPageLocators():
    #лист оформления №1
    #заголовок страницы
    ORDER_HEADER_ONE = (By.XPATH, ".//div[text()='Для кого самокат']")
    #поля заполнения
    PLACEHOLDER_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    PLACEHOLDER_LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    PLACEHOLDER_ADRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    PLACEHOLDER_METRO_STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    STATION_ONE = (By.XPATH, ".//div[text()='Войковская']")
    STATION_TWO = (By.XPATH, ".//div[text()='Спортивная']")
    PLACEHOLDER_PHONE_NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    #кнопка далее
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Далее']")
    #лист оформления №2
    #заголовок страницы
    ORDER_HEADER_TWO = (By.XPATH, ".//div[text()='Про аренду']")
    #поля заполнения
    PLACEHOLDER_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DATE_ONE = (By.XPATH, ".//div[text()='2']")
    DATE_TWO = (By.XPATH, ".//div[text()='30']")
    RENT_TIME = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_TIME_MENU = (By.XPATH, ".//div[@class='Dropdown-menu']")
    RENT_TIME_ONE = (By.XPATH, ".//div[text()='сутки']")
    RENT_TIME_TWO = (By.XPATH, ".//div[text()='двое суток']")
    COLOR_SCOOTER = (By.XPATH, ".//div[text()='Цвет самоката']")
    CHECKBOX_BLACK = (By.ID, "black")
    CHECKBOX_GREY = (By.ID, "grey")
    PLACEHOLDER_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    MIDDLE_BUTTON_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    #лист подтверждения заказа
    ORDER_HEADER_CONFIRM = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, ".//button[text()='Да']")
    #лист успешног оформления
    ORDER_HEADER_SUCCESS = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
