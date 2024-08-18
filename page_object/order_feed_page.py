import allure

from locators.locators_order_feed_page import LocatorsOrderFeedPage
from page_object.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Найти надпись "Выполнено за все время"')
    def find_all_orders_label(self):
        return self.find_element_located(LocatorsOrderFeedPage.ALL_ORDERS_LABEL)

    @allure.step('Нажать на первый заказ в ленте заказов')
    def click_on_first_order(self):
        self.click_on_element(LocatorsOrderFeedPage.FIRST_ORDER)

    @allure.step('Найти слово "Состав" при открытии модального окна заказа')
    def find_order_composition_label(self):
        return self.find_element_located(LocatorsOrderFeedPage.ORDER_COMPOSITION_LABEL)

    @allure.step('Найти надпись "Идентификатор заказа"')
    def get_first_order_number(self):
        return self.find_element_located(LocatorsOrderFeedPage.ORDER_NUMBER).text

    @allure.step('Найти количество заказов за все время')
    def find_all_orders_counter(self):
        return self.find_element_located(LocatorsOrderFeedPage.COUNTER_ALL_ORDERS).text

    @allure.step('Найти количество заказов за сегодня')
    def find_today_orders_counter(self):
        return self.find_element_located(LocatorsOrderFeedPage.COUNTER_TODAY_ORDERS).text

    @allure.step('Найти заказ в работе')
    def find_in_work_order(self):
        return self.find_element_located(LocatorsOrderFeedPage.IN_WORK_ORDER).text
