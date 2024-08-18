from selenium.webdriver.common.by import By


class LocatorsOrderFeedPage:
    ALL_ORDERS_LABEL = (By.XPATH, ".//p[text() = 'Выполнено за все время:']")
    FIRST_ORDER = (By.XPATH, ".//ul[@class = 'OrderFeed_list__OLh59']/li[1]")
    ORDER_COMPOSITION_LABEL = (By.XPATH, ".//p[text() = 'Cостав']")
    ORDER_NUMBER = (By.XPATH, ".//ul/li[1]/a/div/p[@class = 'text text_type_digits-default'][1]")
    COUNTER_ALL_ORDERS = (By.XPATH, ".//p[text() = 'Выполнено за все время:']/parent::div/p[2]")
    COUNTER_TODAY_ORDERS = (By.XPATH, ".//p[text() = 'Выполнено за сегодня:']/parent::div/p[2]")
    IN_WORK_ORDER = (By.XPATH, ".//p[text() = 'В работе:']/parent::div/ul[2]/li")

