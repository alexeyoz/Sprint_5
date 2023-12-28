from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants


class TestLoginAccount:
    # 5. Проверка (вход по кнопке «Войти в аккаунт» на главной)
    def test_login_main_page(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_ACCOUNT).click()  # нажать "Войти в аккаунт"
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)  # ввести тестовый логин
        driver.find_element(*Locators.PASSWORD_FILED).send_keys(Constants.TEST_PASSWORD)  # ввести тестовый пароль
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # нажать "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.PLACE_ORDER))  # ждем
        assert (driver.find_element(*Locators.PLACE_ORDER).is_displayed())  # появилась кнопка "Оформить заказ"

    # 6. Проверка (вход через кнопку «Личный кабинет»)
    def test_login_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)  # ввести тестовый логин
        driver.find_element(*Locators.PASSWORD_FILED).send_keys(Constants.TEST_PASSWORD)  # ввести тестовый пароль
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # нажать "Войти"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.PLACE_ORDER))  # ждем
        assert (driver.find_element(*Locators.PLACE_ORDER).is_displayed())  # появилась кнопка "Оформить заказ"

    # 7. Проверка (вход через кнопку в форме регистрации)
    def test_login_via_registration(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        driver.find_element(*Locators.REGISTRATION).click()  # нажать "Зарегистрироваться"
        driver.find_element(*Locators.LOGIN_VIA_REGISTRATION).click()  # нажать "Войти" в меню регистрации
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)  # ввести тестовый логин
        driver.find_element(*Locators.PASSWORD_FILED).send_keys(Constants.TEST_PASSWORD)  # ввести тестовый пароль
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # нажать "Войти"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.PLACE_ORDER))  # ждем
        assert (driver.find_element(*Locators.PLACE_ORDER).is_displayed())  # появилась кнопка "Оформить заказ"

    # 8. Проверка (вход через кнопку в форме восстановления пароля)
    def test_login_via_password_recovery(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        driver.find_element(*Locators.RECOVER_PASSWORD).click()  # нажать "Восстановить пароль"
        driver.find_element(*Locators.LOGIN_VIA_REGISTRATION).click()  # нажать "Войти" в меню регистрации
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)  # ввести тестовый логин
        driver.find_element(*Locators.PASSWORD_FILED).send_keys(Constants.TEST_PASSWORD)  # ввести тестовый пароль
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # нажать "Войти"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.PLACE_ORDER))  # ждем
        assert (driver.find_element(*Locators.PLACE_ORDER).is_displayed())  # появилась кнопка "Оформить заказ"

    # 9. Проверка (выход по кнопке «Выйти» в личном кабинете.)
    def test_login_account(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_ACCOUNT).click()  # нажать "Войти в аккаунт"
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(Constants.TEST_EMAIL)  # ввести тестовый логин
        driver.find_element(*Locators.PASSWORD_FILED).send_keys(Constants.TEST_PASSWORD)  # ввести тестовый пароль
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # нажать "Войти"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(Locators.OUT_PERSONAL_ACCOUNT))
        driver.find_element(*Locators.OUT_PERSONAL_ACCOUNT).click()  # нажать "Выход" в личном кабинете
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGGING_AFTER_EXITING))
        assert driver.find_element(*Locators.LOGGING_AFTER_EXITING).is_displayed()  # появилась кнопка "Войти"
