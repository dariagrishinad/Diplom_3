from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    LOGIN_TEXT = (By.XPATH, ".//h2[contains(text(), 'Вход')]")
    EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']/parent::div/input")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    AUTH_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")
