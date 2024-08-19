from selenium.webdriver.common.by import By


class LocatorsMainPage:
    LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    PERSONAL_AREA = (By.XPATH, ".//p[text() = 'Личный Кабинет']/parent::a")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']/parent::a")
    COLLECT_BURGER_LABEL = (By.XPATH, ".//h1[text() = 'Соберите бургер']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text() = 'Лента Заказов']/parent::a")
    FIRST_BUN = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']/parent::a")
    DETAILS_OF_INGREDIENT_LABEL = (By.XPATH, ".//h2[text() = 'Детали ингредиента']")
    CLOSE_MODAL_WINDOW_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK")
    MODAL_CLOSE_SECTION = (By.XPATH, ".//section[1]//button[contains(@class, 'Modal_modal__close_modified')]")
    CART_TOP = (By.XPATH, ".//span[text() = 'Перетяните булочку сюда (верх)']")
    COUNTER = (By.XPATH, ".//ul[contains(@class, 'BurgerIngredients_ingredients__list')][1]/a[contains(@class, 'BurgerIngredient_ingredient')][1]//p[text()=2]")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    CREATED_ORDER_LABEL = (By.XPATH, ".//p[text() = 'идентификатор заказа']")



