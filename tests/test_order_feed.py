import allure

from page_object.login_page import LoginPage
from page_object.main_page import MainPage
from page_object.order_feed_page import OrderFeedPage
from page_object.personal_area_page import PersonalAreaPage


class TestOrderFeed:
    @allure.step('Тест открытия окна с описанием заказа при нажатии на заказ')
    def test_click_on_order(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_order_feed()
        order_feed_page.click_on_first_order()

        assert order_feed_page.find_order_composition_label()

    @allure.step('Тест появления созданного заказа в Ленте Заказов')
    def test_check_created_order_in_order_feed(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_area = PersonalAreaPage(driver)
        order_feed = OrderFeedPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        login_page.fill_email_input()
        login_page.fill_password_input()
        login_page.click_on_auth_button()
        main_page.add_ingredient_to_the_cart()
        main_page.click_on_create_order_button()
        main_page.find_created_order_label()
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        personal_area.click_on_history_button()
        order_number = personal_area.find_last_order_number()
        main_page.go_to_order_feed()

        assert order_number == order_feed.get_first_order_number()

    @allure.step('Тест увеличения счетчика заказов за все время')
    def test_counter_of_orders_all_time(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        login_page.fill_email_input()
        login_page.fill_password_input()
        login_page.click_on_auth_button()
        main_page.click_on_order_feed()
        old_orders_count = order_feed.find_all_orders_counter()
        main_page.go_to_main_page()
        main_page.add_ingredient_to_the_cart()
        main_page.click_on_create_order_button()
        main_page.find_created_order_label()
        main_page.go_to_main_page()
        main_page.go_to_order_feed()
        new_orders_count = order_feed.find_all_orders_counter()

        assert int(old_orders_count) + 1 == int(new_orders_count)

    @allure.step('Тест увеличения счетчика заказов за сегодня')
    def test_counter_of_orders_today(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        login_page.fill_email_input()
        login_page.fill_password_input()
        login_page.click_on_auth_button()
        main_page.click_on_order_feed()
        old_today_orders_count = order_feed.find_today_orders_counter()
        main_page.go_to_main_page()
        main_page.add_ingredient_to_the_cart()
        main_page.click_on_create_order_button()
        main_page.find_created_order_label()
        main_page.go_to_main_page()
        main_page.go_to_order_feed()
        new_today_orders_count = order_feed.find_today_orders_counter()

        assert int(old_today_orders_count) + 1 == int(new_today_orders_count)

    @allure.step('Тест нахождения созданного заказа в блоке "В работе" в Ленте Заказов')
    def test_order_feed_in_progress(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_area = PersonalAreaPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        login_page.fill_email_input()
        login_page.fill_password_input()
        login_page.click_on_auth_button()
        main_page.add_ingredient_to_the_cart()
        main_page.click_on_create_order_button()
        main_page.find_created_order_label()
        main_page.go_to_main_page()
        main_page.click_on_personal_area_button()
        personal_area.click_on_history_button()
        order_number = personal_area.find_last_order_number()
        main_page.click_on_order_feed()
        order_in_work = order_feed.find_in_work_order()

        assert order_in_work in order_number
