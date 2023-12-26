from selenium.webdriver.common.by import By


class Locators:
    # поля страницы
    LOGIN_FIELD = (By.XPATH, './/fieldset[1]/*/*/input')                              # поле ввода логина
    PASSWORD_FILED = (By.XPATH, './/fieldset[2]/*/*/input')                           # поле ввода пароля
    NAME_REGISTRATION = (By.XPATH, ".// form / fieldset[1] / div / div / input")      # имя при регистрации
    EMAIL_REGISTRATION = (By.XPATH, ".// form / fieldset[2] / div / div / input")     # email при регистрации
    PASSWORD_REGISTRATION = (By.XPATH, ".// form / fieldset[3] / div / div / input")  # пароль при регистрации

    # кнопки страницы
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, './/section[2]/div/button')                     # войти в аккаунт
    LOGIN_BUTTON = (By.XPATH, './/form/button')                                       # войти после ввода данных
    PLACE_ORDER = (By.XPATH, './/section[2]/div/button')                              # оформить заказ
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//header[1]/nav/a/p")                      # личный кабинет
    REGISTRATION = (By.XPATH, './/p[1]/a')                                            # зарегистрироваться
    LOGIN_VIA_REGISTRATION = (By.XPATH, './/div/p/a')                                 # войти в меню регистрации
    RECOVER_PASSWORD = (By.XPATH, './/p[2]/a')                                        # восстановить пароль
    OUT_PERSONAL_ACCOUNT = (By.XPATH, './/ul/li[3]/button')                           # выход из личного кабинета
    LOGGING_AFTER_EXITING = (By.XPATH, ".//form/button")                              # кнопка войти
    CONSTRUCTOR_BUTTON = (By.XPATH, './/ul / li[1] / a / p')                          # кнопка "Конструктор"
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")               # кнопка "Логотип"
    SAUCES_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[2]")                         # кнопка "Соусы"
    BUNS_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[1]")                           # кнопка "Булки"
    TOPPINGS_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[3]")                       # кнопка "Начинки"

    # ошибки
    INCORRECT_PASSWORD = (By.XPATH, ".//p[contains(text(),'Некорректный пароль')]")   # ошибка при вводе пароля