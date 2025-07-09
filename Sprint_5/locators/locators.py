from selenium.webdriver.common.by import By


class Locators:
    # Кнопка "Войти / Зарегистрироваться" на главной
    LOGIN_REGISTER_BUTTON = (By.XPATH, '/html/body/div/div/div[1]/div/button[1]')

    # Кнопка "У меня нет аккаунта"
    NO_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[2]')

    # Поле "Email"
    EMAIL_INPUT = (By.XPATH, '/html/body/div/div/div[2]/div[5]/form/div[2]/div[1]/div/div/input')

    # Поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, '/html/body/div/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input')

    # Поле "Подтверждение пароля"
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[3]/div/div/input')

    # Кнопка "Создать аккаунт"
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]')

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, '/html/body/div/div/div[2]/div[5]/form/div[3]/button[1]')

    # Кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, '/html/body/div/div/div[1]/div/div[1]/div/button')

    # Кнопка "Разместить объявление" (2)
    POST_AD_BUTTON_2 = (By.XPATH, '/html/body/div/div/div[1]/div/button[2]')

    # Кнопка "Разместить объявление"
    POST_AD_BUTTON = (By.XPATH, '/html/body/div/div/div[1]/div/button')

    # Кнопка "Опубликовать"
    PUBLISH_BUTTON = (By.XPATH, '/html/body/div/div/div[2]/div/form/button')

    # Аватар пользователя
    USER_AVATAR = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/button')

    # Заголовок модального окна
    MODAL_HEADER = (By.XPATH, '/html/body/div/div/div[2]/div[5]/form/div[1]/h1')

    # Имя пользователя
    USER_NAME = (By.XPATH, '/html/body/div/div/div[1]/div/div[1]/div/h3')

    # Сообщение об ошибке Email
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//span[contains(text(),'Ошибка')]")

    # Поле "Название объявления"
    AD_TITLE_INPUT = (By.XPATH, '/html/body/div/div/div[2]/div/form/div[2]/div[1]/div/div/input')

    # Поле "Описание объявления"
    AD_DESCRIPTION_INPUT = (By.XPATH, '/html/body/div/div/div[2]/div/form/div[4]/div/textarea')

    # Поле "Цена"
    AD_PRICE_INPUT = (By.XPATH, '/html/body/div/div/div[2]/div/form/div[5]/div/div/input')

    # Дропдаун категории
    AD_CATEGORY_DROPDOWN = (By.XPATH, '/html/body/div/div/div[2]/div/form/div[2]/div[2]/div[1]/button')

    # Дропдаун города
    AD_CITY_DROPDOWN = (By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/div[1]/button')

    # Радиокнопка "Новое состояние"
    AD_CONDITION_NEW_RADIO = (By.XPATH, '/html/body/div/div/div[2]/div/form/fieldset/div/div[2]/div')

    # Секция объявлений пользователя
    USER_ADS_SECTION = (By.CSS_SELECTOR, "div.grid_threeColumns__ldn5D")

    # Заголовок объявления пользователя
    USER_AD_TITLE = (By.CSS_SELECTOR, "div.card div.about > h2.h2")

    # Опция категории в дропдауне
    AD_CATEGORY_OPTION = (By.XPATH, '/html/body/div/div/div[2]/div/form/div[2]/div[2]/div[2]/button[2]')

    # Опция города в дропдауне
    AD_CITY_OPTION = (By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/div[2]/button[2]')

    HOME_PAGE = (By.XPATH, "//*[contains(@class, 'homePage_homepage')]")
