import pytest
from selenium import webdriver
import random
from constants import Constants


# драйвер
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.BASE_URL)
    yield driver
    driver.quit()


# создание данных для регистрации
@pytest.fixture
def generate_registration_data():
    name = 'alexeyv'
    email = f"{name}{4}{random.randint(100, 999)}@ya.ru"
    password = random.randint(100000, 999999)
    return name, email, password
