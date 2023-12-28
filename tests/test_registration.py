from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestRegOnSite:
    # 1. Проверка успешной регистрации
    def test_successful_registration(self, driver, generate_registration_data):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        driver.find_element(*Locators.REGISTRATION).click()  # нажать "Зарегистрироваться"
        driver.find_element(*Locators.NAME_REGISTRATION).send_keys(generate_registration_data[0])  # ввод имя
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(generate_registration_data[1])  # ввод email
        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(generate_registration_data[2])  # ввод пароль
        driver.find_element(*Locators.REGISTRATION).click()  # нажать "Зарегистрироваться"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))  # ждем
        assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()  # проверка наличия кнопки "Войти"

    # 2. Проверка регистрации без имени
    def test_registration_without_name(self, driver, generate_registration_data):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        driver.find_element(*Locators.REGISTRATION).click()  # нажать "Зарегистрироваться"
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(generate_registration_data[1])  # ввод email
        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(generate_registration_data[2])  # ввод пароль
        driver.find_element(*Locators.REGISTRATION).click()  # нажать "Зарегистрироваться"
        assert driver.find_element(*Locators.REGISTRATION).is_displayed()  # проверка ничего не изменилось

    # 3. Проверка некорректный email
    def test_registration_incorrect_email(self, driver, generate_registration_data):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        driver.find_element(*Locators.REGISTRATION).click()  # нажать "Зарегистрироваться"
        driver.find_element(*Locators.NAME_REGISTRATION).send_keys(generate_registration_data[0])  # ввод имя
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys('alexeyvasiliev4000yandex.ru')  # ввод кривой email
        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys(generate_registration_data[2])  # ввод пароль
        driver.find_element(*Locators.REGISTRATION).click()  # нажать "Зарегистрироваться"
        assert driver.find_element(*Locators.REGISTRATION).is_displayed()  # проверка ничего не изменилось

    # 4. Проверка некорректный пароль
    def test_registration_incorrect_password(self, driver, generate_registration_data):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        driver.find_element(*Locators.REGISTRATION).click()  # нажать "Зарегистрироваться"
        driver.find_element(*Locators.NAME_REGISTRATION).send_keys(generate_registration_data[0])  # ввод имя
        driver.find_element(*Locators.EMAIL_REGISTRATION).send_keys(generate_registration_data[1])  # ввод email
        driver.find_element(*Locators.PASSWORD_REGISTRATION).send_keys('12345')  # ввод пароль 5 символов
        driver.find_element(*Locators.REGISTRATION).click()  # нажать "Зарегистрироваться"
        assert driver.find_element(*Locators.INCORRECT_PASSWORD).is_displayed()  # проверка отображения ошибки
