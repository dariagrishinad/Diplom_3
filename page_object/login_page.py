import allure

from constants import Constants
from locators.locators_login_page import LocatorsLoginPage
from page_object.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Клик по ссылке восстановления пароля')
    def click_on_restore_password_link(self):
        self.click_on_element(LocatorsLoginPage.RESTORE_PASSWORD_LINK)

    @allure.step('Поиск текста "Вход" в форме авторизации')
    def find_enter_label(self):
        return self.find_element_located(LocatorsLoginPage.LOGIN_TEXT)

    @allure.step('Заполнение инпута email')
    def fill_email_input(self):
        self.fill_input(Constants.EMAIL, LocatorsLoginPage.EMAIL_INPUT)

    @allure.step('Заполнения инпута Пароль')
    def fill_password_input(self):
        self.fill_input(Constants.PASSWORD, LocatorsLoginPage.PASSWORD_INPUT)

    @allure.step('Клик по кнопке "Войти" в форме авторизации')
    def click_on_auth_button(self):
        self.click_on_element(LocatorsLoginPage.AUTH_BUTTON)
