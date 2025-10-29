from selenium.webdriver.common.by import By


class MainPageLocators():
    #кнопка "Заказать" в центре страницы
    MIDDLE_BUTTON_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    #вопросы о важном(вопросы)
    QUESTION_1 = (By.ID, "accordion__heading-24")
    QUESTION_2 = (By.ID, "accordion__heading-25")
    QUESTION_3 = (By.ID, "accordion__heading-26")
    QUESTION_4 = (By.ID, "accordion__heading-27")
    QUESTION_5 = (By.ID, "accordion__heading-28")
    QUESTION_6 = (By.ID, "accordion__heading-29")
    QUESTION_7 = (By.ID, "accordion__heading-30")
    QUESTION_8 = (By.ID, "accordion__heading-31")
    #вопросы о важном(ответы)
    ANSWER_1 = (By.XPATH, ".//div[@id='accordion__panel-24']/p")
    ANSWER_2 = (By.XPATH, ".//div[@id='accordion__panel-25']/p")
    ANSWER_3 = (By.XPATH, ".//div[@id='accordion__panel-26']/p")
    ANSWER_4 = (By.XPATH, ".//div[@id='accordion__panel-27']/p")
    ANSWER_5 = (By.XPATH, ".//div[@id='accordion__panel-28']/p")
    ANSWER_6 = (By.XPATH, ".//div[@id='accordion__panel-29']/p")
    ANSWER_7 = (By.XPATH, ".//div[@id='accordion__panel-30']/p")
    ANSWER_8 = (By.XPATH, ".//div[@id='accordion__panel-31']/p")
