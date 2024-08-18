from selenium.webdriver.common.by import By


class LocatorsPersonalAreaPage:
    HISTORY_ORDERS = (By.XPATH, ".//a[text() = 'История заказов']")
    HISTORY_LABEL_ACTIVE = (By.CLASS_NAME, "Account_link_active__2opc9")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
    LOGIN_TEXT = (By.XPATH, ".//h2[text() = 'Вход']")
    LAST_ORDER = (By.XPATH, ".//ul[@class = 'OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[last()]/a/div/p[1]")