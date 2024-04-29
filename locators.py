from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()= 'Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()= 'Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    REGISTRATION_NAME_INPUT = (By.XPATH, "//label[text() = 'Имя']/../input")  # поле "Имя" в форме регистрации
    REGISTRATION_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/../input")  # поле "Email" в форме регистрации
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, "//label[text() = 'Пароль']/../input")  # поле "Пароль" в форме регистрации
    CONFIRM_REGISTRATION_BUTTON = (By.XPATH, "//button[text()= 'Зарегистрироваться']")  # кнопка подтверждения регистрации
    LOGIN_BUTTON = (By.XPATH, "//button[text()= 'Войти']")  # кнопка "Войти" при авторизации
    INCORRECT_PASSWORD_TEXT = (By.XPATH, ".//p[@class='input__error text_type_main-default']")  # текст "Некорректный пароль"
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()= 'Личный Кабинет']") # кнопка "Личный кабинет"
    LOGIN_BUTTON_IN_REGISTRATION_FORM = (By.XPATH, "//a[text()= 'Войти']") # кнопка "Войти" в форме регистрации
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()= 'Восстановить пароль']") # кнопка "Восстановить пароль"
    AUTH_EMAIL_INPUT = (By.NAME, "name")  # поле "Email" при авторизации
    AUTH_PASSWORD_INPUT = (By.NAME, "Пароль")  # поле "Пароль" при авторизации
    PROFILE_BUTTON = (By.XPATH, "//a[contains(.,'Профиль')]")  # кнопка "История заказов"
    EXIT_PERSONAL_CABINET = (By.XPATH, "//button[text()= 'Выход']")  # кнопка "Выход"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")  # кнопка "Конструктор"
    BURGER_TEXT = (By.XPATH, "//h1[text()= 'Соберите бургер']")  # кнопка "Соберите бургер"
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # кнонка логотип
    SAUCES_LOCATION_BUTTON = (By.XPATH, "//span[text() = 'Соусы']") # кнопка "Соусы"
    SAUCES_PARRENT_CLASS = (By.XPATH, "//span[text()= 'Соусы']/parent::div")
    CURRENT_SECTION = (By.XPATH, "//div[@class= 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']",)  # класс выбранного раздела
    FILLINGS_LOCATION_BUTTON = (By.XPATH, "//span[text() = 'Начинки']") # кнопка "Начинки"
    FILLINGS_PARRENT_CLASS = (By.XPATH, "//span[text()= 'Начинки']/parent::div")
    BUNS_LOCATION_BUTTON = (By.XPATH, "//span[text()= 'Булки']") # кнопка "Булки"
    BUNS_PARRENT_CLASS = (By.XPATH, "//span[text()= 'Булки']/parent::div")
    LOGIN_BUTTON_IN_RESTORE_PASSWORD = (By.XPATH, "//a[text()= 'Войти']") #кнопка "Войти" в разделе восстановления пароля
