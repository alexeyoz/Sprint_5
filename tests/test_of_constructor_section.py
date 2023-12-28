from locators import Locators


class TestConstructor:
    # 13. Проверка перехода к разделу "Соусы"
    def test_sauces_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        assert "current" in (driver.find_element(*Locators.SAUCES_BUTTON).get_attribute("class"))

    # 14. Проверка перехода к разделу "Начинки"
    def test_toppings_section(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        assert "current" in (driver.find_element(*Locators.TOPPINGS_BUTTON).get_attribute("class"))

    # 15. Проверка перехода к разделу "Булки"
    def test_bread_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        assert "current" in (driver.find_element(*Locators.BUNS_BUTTON).get_attribute("class"))
