import allure

from page_object.login_page import LoginPage
from page_object.main_page import MainPage
from page_object.restore_password_page import RestorePasswordPage


class TestRestorePassword:
    @allure.step('Тест нажатия на кнопку "Восстановить пароль"')
    def test_restore_password_click_on_restore_password_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        restore_password_page = RestorePasswordPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_login_button()
        main_page.scroll()
        login_page.click_on_restore_password_link()

        assert restore_password_page.find_text_restore_password()

    @allure.step('Тест заполнения формы восстановления пароля')
    def test_restore_password_enter_email_and_click_on_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        restore_password_page = RestorePasswordPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_login_button()
        main_page.scroll()
        login_page.click_on_restore_password_link()
        restore_password_page.enter_email_field()
        restore_password_page.click_on_restore_button()

        assert restore_password_page.find_label_at_restore_password()

    @allure.step('Тест отображения пароля при нажатии на иконку глаза')
    def test_restore_password_click_on_hide_password_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        restore_password_page = RestorePasswordPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_login_button()
        main_page.scroll()
        login_page.click_on_restore_password_link()
        restore_password_page.enter_email_field()
        restore_password_page.click_on_restore_button()
        restore_password_page.enter_password_field()
        restore_password_page.click_on_hide_password_button()

        assert restore_password_page.find_shown_password()
