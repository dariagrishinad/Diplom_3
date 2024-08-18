import allure

from locators.locators_personal_area_page import LocatorsPersonalAreaPage
from page_object.base_page import BasePage


class PersonalAreaPage(BasePage):
    @allure.step('Нажать на кнопку "История заказов"')
    def click_on_history_button(self):
        self.click_on_element(LocatorsPersonalAreaPage.HISTORY_ORDERS)

    @allure.step('Найти новый класс у надписи "История заказов"')
    def find_new_class_history_label(self):
        return self.find_element_located(LocatorsPersonalAreaPage.HISTORY_LABEL_ACTIVE)

    @allure.step('Нажать на кнопку "Выйти"')
    def click_on_logout_button(self):
        self.click_on_element(LocatorsPersonalAreaPage.LOGOUT_BUTTON)

    @allure.step('Найти надпись "Вход" в форме авторизации')
    def find_login_label(self):
        return self.find_element_located(LocatorsPersonalAreaPage.LOGIN_TEXT)

    @allure.step('Найти последний сделанный заказ')
    def find_last_order_number(self):
        return self.find_element_located(LocatorsPersonalAreaPage.LAST_ORDER).text

