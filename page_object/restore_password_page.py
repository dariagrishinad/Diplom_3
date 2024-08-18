import allure

from constants import Constants
from locators.locators_restore_password_page import LocatorsRestorePasswordPage
from page_object.base_page import BasePage


class RestorePasswordPage(BasePage):
    @allure.step('Заполнить инпут email')
    def enter_email_field(self):
        self.fill_input(Constants.EMAIL, LocatorsRestorePasswordPage.EMAIL_FOR_RESTORE_PASSWORD)

    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_on_restore_button(self):
        self.click_on_element(LocatorsRestorePasswordPage.BUTTON_FOR_RESTORE_PASSWORD)

    @allure.step('Найти кнопку "Восстановить"')
    def find_text_restore_password(self):
        return self.find_element_located(LocatorsRestorePasswordPage.BUTTON_FOR_RESTORE_PASSWORD)

    @allure.step('Найти надпись "Введите код из письма"')
    def find_label_at_restore_password(self):
        return self.find_element_located(LocatorsRestorePasswordPage.LABEL_FOR_RESTORE_PASSWORD)

    @allure.step('Заполнить поле Пароль')
    def enter_password_field(self):
        self.fill_input(Constants.PASSWORD, LocatorsRestorePasswordPage.PASSWORD_INPUT_FOR_RESTORE_PASSWORD)

    @allure.step('Нажать на иконку глаза')
    def click_on_hide_password_button(self):
        self.click_on_element(LocatorsRestorePasswordPage.BUTTON_HIDE_PASSWORD)

    @allure.step('Найти отображенный пароль')
    def find_shown_password(self):
        return self.find_element_located(LocatorsRestorePasswordPage.LABEL_FOR_SHOWN_PASSWORD)