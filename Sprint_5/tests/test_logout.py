import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators.locators import Locators
from Sprint_5.conftest import driver, logged_in_user, registered_user


@pytest.mark.usefixtures("driver")
class TestLogout:

    # Logout пользователя
    def test_user_can_logout(self, driver, logged_in_user):
        wait = WebDriverWait(driver, 15)

        wait.until(EC.presence_of_element_located(Locators.HOME_PAGE))

        avatar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.USER_AVATAR))
        avatar.click()

        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON))
        assert login_button.is_displayed(), "Ожидалась доступность кнопки входа после выхода"