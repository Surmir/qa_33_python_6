from selenium.webdriver.common.by import By


class BasePageLocators():

    HEADER_LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']")
    HEADER_LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")
    HEADER_BUTTON_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
