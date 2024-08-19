from selenium.webdriver.common.by import By


class LocatorsRestorePasswordPage:
    EMAIL_FOR_RESTORE_PASSWORD = (By.XPATH, ".//label[text() = 'Email']/parent::div/input")  # Инпут с email для восстановления пароля
    BUTTON_FOR_RESTORE_PASSWORD = (By.XPATH, ".//button[text() = 'Восстановить']")
    LABEL_FOR_RESTORE_PASSWORD = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    PASSWORD_INPUT_FOR_RESTORE_PASSWORD = (By.XPATH, ".//input[@name = 'Введите новый пароль']")
    BUTTON_HIDE_PASSWORD = (By.CLASS_NAME, "input__icon-action")
    LABEL_FOR_SHOWN_PASSWORD = (By.CLASS_NAME, "input__placeholder-focused")

