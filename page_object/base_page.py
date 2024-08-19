import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Зайти на сайт')
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    @allure.step('Проверить наличие элемента на сайте')
    def find_element_located(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

    @allure.step('Кликнуть по кликабельному элементу')
    def click_on_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Проскроллить страницу')
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    @allure.step('Заполнить инпут')
    def fill_input(self, text, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys(text)

    @allure.step('Получить url текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переход на новую открытую вкладку')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получение аттрибута элемента')
    def get_attribute_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).get_attribute("class")

    @allure.step('Drag and drop')
    def drag_and_drop(self, element, target):
        action_chains = ActionChains(self.driver)
        add_element = self.find_element_located(element)
        add_target = self.find_element_located(target)
        action_chains.drag_and_drop(add_element, add_target).perform()

