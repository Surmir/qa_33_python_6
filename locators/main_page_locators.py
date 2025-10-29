from selenium.webdriver.common.by import By


class MainPageLocators():
    #заголовок страницы
    MAIN_HEADER = (By.CLASS_NAME, "Home_Header__iJKdX")
    #кнопка "Заказать" в центре страницы
    MIDDLE_BUTTON_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    #вопросы о важном(вопросы)
    QUESTION_1 = (By.ID, "accordion__heading-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")
    #вопросы о важном(ответы)
    ANSWER_1 = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    ANSWER_2 = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    ANSWER_3 = (By.XPATH, ".//div[@id='accordion__panel-2']/p")
    ANSWER_4 = (By.XPATH, ".//div[@id='accordion__panel-3']/p")
    ANSWER_5 = (By.XPATH, ".//div[@id='accordion__panel-4']/p")
    ANSWER_6 = (By.XPATH, ".//div[@id='accordion__panel-5']/p")
    ANSWER_7 = (By.XPATH, ".//div[@id='accordion__panel-6']/p")
    ANSWER_8 = (By.XPATH, ".//div[@id='accordion__panel-7']/p")
