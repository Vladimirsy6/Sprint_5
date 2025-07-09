import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators.locators import Locators
from Sprint_5.conftest import driver

class TestRegistration:

    # Регистрация пользователя
    def test_registration_success(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        email = f"user_{int(time.time())}@test.com"
        password = "Qwerty123!"

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        avatar = wait.until(EC.visibility_of_element_located(Locators.USER_AVATAR))
        assert avatar.is_displayed(), "Аватар пользователя не отображается после успешной регистрации"

        user_name = wait.until(EC.visibility_of_element_located(Locators.USER_NAME))
        assert user_name.text == "User.", f"Ожидалось имя 'User.', получили '{user_name.text}'"

        assert "qa-desk.stand.praktikum-services.ru" in driver.current_url, "Не произошёл переход на главную после регистрации"

    # Регистрация пользователя c email не по маске  *******@*******.***
    def test_registration_invalid_email(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        invalid_email = "invalid_email"
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(invalid_email)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_message = wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert error_message.is_displayed(), "Сообщение об ошибке под Email не отображается"

        assert driver.find_element(*Locators.EMAIL_INPUT).is_enabled(), "Поле Email недоступно после ошибки"
        assert driver.find_element(*Locators.PASSWORD_INPUT).is_enabled(), "Поле Password недоступно после ошибки"
        assert driver.find_element(*Locators.CONFIRM_PASSWORD_INPUT).is_enabled(), "Поле Confirm Password недоступно после ошибки"

    # Регистрация уже существующего пользователя
    def test_registration_existing_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        existing_email = "existing_user@example.com"
        password = "ValidPassword123"

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(existing_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        # Проверяем появление сообщения об ошибке
        error_message = wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert error_message.is_displayed(), "Сообщение об ошибке под Email не отображается при регистрации существующего пользователя"

        # Проверяем выделение полей красным
        def is_red_color(color):
            import re
            match = re.match(r'rgba?\((\d+), (\d+), (\d+)', color)
            if not match:
                return False
            r, g, b = map(int, match.groups())
            return r >= 200 and g <= 120 and b <= 120

        email_border = driver.find_element(*Locators.EMAIL_INPUT).value_of_css_property("border-color")
        password_border = driver.find_element(*Locators.PASSWORD_INPUT).value_of_css_property("border-color")
        confirm_border = driver.find_element(*Locators.CONFIRM_PASSWORD_INPUT).value_of_css_property("border-color")
        error_color = error_message.value_of_css_property("color")

        assert is_red_color(email_border) or is_red_color(error_color), "Поле Email не выделяется красным при ошибке"
        assert is_red_color(password_border) or is_red_color(
            error_color), "Поле Password не выделяется красным при ошибке"
        assert is_red_color(confirm_border) or is_red_color(
            error_color), "Поле Confirm Password не выделяется красным при ошибке"

