from selenium.webdriver.common.by import By


class Locators:
    # поля страницы
    LOGIN_FIELD = (By.XPATH, ".//*[@name='name']")  # поле ввода логина
    PASSWORD_FILED = (By.XPATH, ".//*[@name='Пароль']")  # поле ввода пароля
    NAME_REGISTRATION = (By.XPATH, "//label[text()='Имя']/following-sibling::*")  # имя при регистрации
    EMAIL_REGISTRATION = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # email при регистрации
    PASSWORD_REGISTRATION = (By.XPATH, ".//*[@name='Пароль']")  # пароль при регистрации

    # кнопки страницы
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # войти в аккаунт
    LOGIN_BUTTON = (By.XPATH, './/form/button')  # войти после ввода данных
    PLACE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  # оформить заказ
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # личный кабинет
    REGISTRATION = (By.XPATH, ".//*[text()='Зарегистрироваться']")  # зарегистрироваться
    LOGIN_VIA_REGISTRATION = (By.XPATH, './/div/p/a')  # войти в меню регистрации
    RECOVER_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")  # восстановить пароль
    OUT_PERSONAL_ACCOUNT = (By.XPATH, "//button[text()='Выход']")  # выход из личного кабинета
    LOGGING_AFTER_EXITING = (By.XPATH, ".//form/button")  # кнопка войти
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # кнопка "Логотип"

    SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']/parent::*")  # кнопка "Соусы"
    BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']/parent::*")  # кнопка"Булки"
    TOPPINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']/parent::*")  # кн."Начинки"

    # ошибки
    INCORRECT_PASSWORD = (By.XPATH, ".//p[contains(text(),'Некорректный пароль')]")  # ошибка при вводе пароля

