import pytest
from selenium import webdriver
import time
from Sprint_5.locators.locators import Locators

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    driver.get(BASE_URL)
    driver.find_element(*Locators.LOGIN_REGISTER_BUTTON).click()
    driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()

    email = f"user_{int(time.time())}@test.com"
    password = "Qwerty123!"

    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.CONFIRM_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

    return email, password

@pytest.fixture
def logged_in_user(driver, registered_user):
    email, password = registered_user

    driver.get(BASE_URL)
    driver.find_element(*Locators.LOGIN_REGISTER_BUTTON).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    return email, password