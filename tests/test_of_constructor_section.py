import time

from locators import Locators


class TestConstructor:
    # 13. Проверка перехода к разделу "Соусы"
    def test_sauces_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        assert driver.find_element(*Locators.SWITCHING_TO_SAUCES).is_displayed()  # проверка перехода "Соусы"

    # 14. Проверка перехода к разделу "Начинки"
    def test_toppings_section(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        assert driver.find_element(*Locators.SWITCHING_TO_TOPPINGS).is_displayed()  # проверка перехода "Начинки"

    # 15. Проверка перехода к разделу "Булки"
    def test_bread_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        assert driver.find_element(*Locators.SWITCHING_TO_BUNS).is_displayed()  # проверка перехода "Булки"
