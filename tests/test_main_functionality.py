import allure

from page_object.login_page import LoginPage
from page_object.main_page import MainPage
from page_object.order_feed_page import OrderFeedPage


class TestMainFunctionality:
    @allure.step('Тест перехода по кнопке "Конструктор"')
    def test_transform_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        main_page.click_on_constructor_button()

        assert main_page.find_constructor_label()

    @allure.step('Тест перехода по кнопке "Лента заказов"')
    def test_transform_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_order_feed()

        assert order_feed_page.find_all_orders_label()

    @allure.step('Тест нажатия на ингредиент')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient()

        assert main_page.find_ingredient_details_label()

    @allure.step('Тест нажатия на крестик в окне информации об ингредиенте')
    def test_click_on_close_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient()
        main_page.click_on_close_button_in_modal_window()

        assert 'Modal_modal_opened__3ISw4' not in main_page.find_modal_window_closed()

    @allure.step('Тест увеличения счетчика после добавления ингредиента в корзину')
    def test_counter_of_ingredient_after_add_to_the_cart(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.add_ingredient_to_the_cart()

        assert main_page.find_counter()

    @allure.step('Тест оформления заказа под авторизованным пользователем')
    def test_login_user_can_create_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        login_page.fill_email_input()
        login_page.fill_password_input()
        login_page.click_on_auth_button()
        main_page.add_ingredient_to_the_cart()
        main_page.click_on_create_order_button()

        assert main_page.find_created_order_label()
