import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators.locators import Locators
from Sprint_5.conftest import driver, registered_user

@pytest.mark.usefixtures("driver")
class TestLogin:

    # Login пользователя
    def test_user_can_login(self, driver, registered_user):
        email, password = registered_user
        wait = WebDriverWait(driver, 15)

        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*Locators.LOGIN_REGISTER_BUTTON).click()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        avatar = wait.until(EC.presence_of_element_located(Locators.USER_AVATAR))
        assert avatar.is_displayed(), "Ожидалось, что аватар будет отображаться после входа"

        user_name = wait.until(EC.visibility_of_element_located(Locators.USER_NAME))
        assert user_name.text == "User.", f"Ожидалось имя 'User.', получили '{user_name.text}'"