from selenium.webdriver.common.by import By


class Locators:
    # Кнопка "Войти / Зарегистрироваться" на главной
    LOGIN_REGISTER_BUTTON = (By.XPATH, '//button[text()="Вход и регистрация"]')

    # Кнопка "У меня нет аккаунта"
    NO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Нет аккаунта"]')

    # Поле "Email"
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")

    # Поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")

    # Поле "Подтверждение пароля"
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@name='submitPassword']")

    # Кнопка "Создать аккаунт"
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Создать аккаунт')]")

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Войти')]")

    # Кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and text()='Выйти']")

    # Кнопка "Разместить объявление" (2)
    POST_AD_BUTTON_2 = (By.XPATH, "//button[@type='button' and contains(text(), 'Разместить объявление')]")

    # Кнопка "Разместить объявление"
    POST_AD_BUTTON = (By.XPATH, "//button[@type='button' and contains(text(), 'Разместить объявление')]")

    # Кнопка "Опубликовать"
    PUBLISH_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Опубликовать')]")

    # Аватар пользователя
    USER_AVATAR = (By.XPATH, "//button[contains(@class, 'circleSmall')]")

    # Заголовок модального окна
    MODAL_HEADER = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление')]")

    # Имя пользователя
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")

    # Сообщение об ошибке Email
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//span[contains(text(),'Ошибка')]")

    # Поле "Название объявления"
    AD_TITLE_INPUT = (By.XPATH, "//input[@name='name']")

    # Поле "Описание объявления"
    AD_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")

    # Поле "Цена"
    AD_PRICE_INPUT = (By.XPATH, "//input[@name='price']")

    # Дропдаун категории
    AD_CATEGORY_DROPDOWN = (By.XPATH, "//button[contains(@class, 'dropDownMenu_arrowDown')]")

    # Дропдаун города
    AD_CITY_DROPDOWN = (By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[2]")

    # Радиокнопка "Новое состояние"
    AD_CONDITION_NEW_RADIO = (By.XPATH, "(//div[contains(@class, 'radioUnput_inputActive__eC-HY')])[1]")

    # Секция объявлений пользователя
    USER_ADS_SECTION = (By.CSS_SELECTOR, "div.grid_threeColumns__ldn5D")

    # Заголовок объявления пользователя
    USER_AD_TITLE = (By.CSS_SELECTOR, "div.card div.about > h2.h2")

    # Опция категории в дропдауне
    AD_CATEGORY_OPTION = (By.XPATH, "//button[./span[contains(text(), 'Книги')]]")

    # Опция города в дропдауне
    AD_CITY_OPTION = (By.XPATH, "//button[./span[contains(text(), 'Санкт-Петербург')]]")

    HOME_PAGE = (By.XPATH, "//*[contains(@class, 'homePage_homepage')]")
