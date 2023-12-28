from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants


class TestTransitionsButton:
    # 10. Проверка перехода по клику на «Личный кабинет».
    def test_switching_to_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_URL))  # Ждем
        assert driver.current_url == Constants.LOGIN_URL  # Проверяем переход на url

    # 11. Проверка перехода по клику на «Конструктор» из личного кабинета
    def test_switching_to_constructor(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()  # нажать "Конструктор"
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN_ACCOUNT))  # ждем
        assert (driver.find_element(*Locators.BUTTON_LOGIN_ACCOUNT).is_displayed())  # появилась кнопка "Войти в акк."

    # 12. Проверка перехода по клику на «Stellar Burgers» из личного кабинета
    def test_to_logo_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()  # нажать "Личный кабинет"
        driver.find_element(*Locators.LOGO).click()  # нажать логотип "Stellar Burgers"
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN_ACCOUNT))  # ждем
        assert (driver.find_element(*Locators.BUTTON_LOGIN_ACCOUNT).is_displayed())  # появилась кнопка "Войти в акк."
