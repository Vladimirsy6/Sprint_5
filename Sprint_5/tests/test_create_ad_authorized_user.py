import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators.locators import Locators
from Sprint_5.conftest import driver, logged_in_user, registered_user


class TestCreateAd:

    #Создание объявления авторизованным пользователем
    def test_create_ad_authorized_user(self, driver, logged_in_user):
        wait = WebDriverWait(driver, 15)

        # Проверка успешного входа
        avatar = wait.until(EC.presence_of_element_located(Locators.USER_AVATAR))
        assert avatar.is_displayed(), "Аватар не отображается после входа"
        user_name = wait.until(EC.visibility_of_element_located(Locators.USER_NAME))
        assert user_name.text == "User.", f"Ожидалось имя 'User.', получили '{user_name.text}'"

        # Создание объявления
        driver.find_element(*Locators.POST_AD_BUTTON).click()
        driver.find_element(*Locators.AD_TITLE_INPUT).send_keys("Тестовое объявление")
        driver.find_element(*Locators.AD_DESCRIPTION_INPUT).send_keys("Описание товара для теста")
        driver.find_element(*Locators.AD_PRICE_INPUT).send_keys("1500")

        driver.find_element(*Locators.AD_CATEGORY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(Locators.AD_CATEGORY_OPTION)).click()

        driver.find_element(*Locators.AD_CITY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(Locators.AD_CITY_OPTION)).click()

        driver.find_element(*Locators.AD_CONDITION_NEW_RADIO).click()
        driver.find_element(*Locators.PUBLISH_BUTTON).click()

        # Скролл вверх и переход в профиль
        driver.execute_script("window.scrollTo(0, 0);")
        wait.until(EC.presence_of_element_located(Locators.HOME_PAGE))
        wait.until(EC.element_to_be_clickable(Locators.USER_AVATAR)).click()

        # Ждём загрузки профиля и раздела объявлений
        my_ads_section = wait.until(EC.presence_of_element_located(Locators.USER_ADS_SECTION))

        # Считываем заголовки объявлений
        ad_titles = my_ads_section.find_elements(*Locators.USER_AD_TITLE)
        titles_text = [el.text for el in ad_titles]
        print(titles_text)  # можно убрать после стабилизации теста

        assert any("Тестовое объявление" in title for title in titles_text), \
            "Созданное объявление не отображается в профиле"

    #Создание объявления неавторизованным пользователем
    def test_create_ad_unauthorized_user(self, driver):
        wait = WebDriverWait(driver, 15)

        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*Locators.POST_AD_BUTTON_2).click()

        modal_title = wait.until(EC.visibility_of_element_located(Locators.MODAL_HEADER))
        assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь", \
            f"Ожидался заголовок модального окна 'Чтобы разместить объявление, авторизуйтесь', но получили '{modal_title.text}'"