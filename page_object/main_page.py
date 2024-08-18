import allure

from constants import Urls
from locators.locators_main_page import LocatorsMainPage
from page_object.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Перейти на главную страницу сайта')
    def go_to_main_page(self):
        self.go_to_site(Urls.MAIN_URL)

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_on_login_button(self):
        self.click_on_element(LocatorsMainPage.LOGIN_TO_ACCOUNT)

    @allure.step('Клик по кнопке "Личный Кабинет"')
    def click_on_personal_area_button(self):
        self.click_on_element(LocatorsMainPage.PERSONAL_AREA)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(LocatorsMainPage.CONSTRUCTOR_BUTTON)

    @allure.step('Найти надпись "Соберите бургер"')
    def find_constructor_label(self):
        return self.find_element_located(LocatorsMainPage.COLLECT_BURGER_LABEL)

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_on_order_feed(self):
        self.click_on_element(LocatorsMainPage.ORDER_FEED_BUTTON)

    @allure.step('Клик по ингредиенту')
    def click_on_ingredient(self):
        self.click_on_element(LocatorsMainPage.FIRST_BUN)

    @allure.step('Найти надпись "Детали ингредиента"')
    def find_ingredient_details_label(self):
        return self.find_element_located(LocatorsMainPage.DETAILS_OF_INGREDIENT_LABEL)

    @allure.step('Клик по кнопке закрытия модального окна')
    def click_on_close_button_in_modal_window(self):
        self.click_on_element(LocatorsMainPage.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step('Определение закрытия модального окна с помощью класса')
    def find_modal_window_closed(self):
        return self.get_attribute_of_element(LocatorsMainPage.MODAL_CLOSE_SECTION)

    @allure.step('Добавление ингредиента в корзину')
    def add_ingredient_to_the_cart(self):
        self.drag_and_drop(LocatorsMainPage.FIRST_BUN, LocatorsMainPage.CART_TOP)

    @allure.step('Поиск счетчика добавленного элемента в корзину')
    def find_counter(self):
        return self.find_element_located(LocatorsMainPage.COUNTER)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_create_order_button(self):
        self.click_on_element(LocatorsMainPage.CREATE_ORDER_BUTTON)

    @allure.step('Найти надпись "Идентификатор заказа"')
    def find_created_order_label(self):
        return self.find_element_located(LocatorsMainPage.CREATED_ORDER_LABEL)

    @allure.step('Переход в Ленту Заказов')
    def go_to_order_feed(self):
        self.go_to_site(Urls.ORDER_FEED_URL)
