import allure

from page_object.login_page import LoginPage
from page_object.main_page import MainPage
from page_object.personal_area_page import PersonalAreaPage


class TestPersonalArea:
    @allure.step('Тест нажатия на кнопку "Личный Кабинет"')
    def test_click_personal_area_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()

        assert login_page.find_enter_label()

    @allure.step('Тест перехода на вкладку "История заказов" в личном кабинете')
    def test_transform_to_orders_history(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_area = PersonalAreaPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        login_page.fill_email_input()
        login_page.fill_password_input()
        login_page.click_on_auth_button()
        main_page.click_on_personal_area_button()
        personal_area.click_on_history_button()

        assert personal_area.find_new_class_history_label()

    @allure.step('Тест выхода из личного кабинета')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_area = PersonalAreaPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        login_page.fill_email_input()
        login_page.fill_password_input()
        login_page.click_on_auth_button()
        main_page.click_on_personal_area_button()
        personal_area.click_on_logout_button()

        assert personal_area.find_login_label()
