from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
from data import StellarBurgersTestData
import urls


class TestStellarBurgersGoToDifferentSections:

    # Переход "Личный кабинет"
    def test_go_to_personal_cabinet(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellarBurgersTestData.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (StellarBurgersLocators.PROFILE_BUTTON)
            )
        )
        success_url = driver.current_url
        assert success_url == urls.PERSONAL_CABINET_PAGE_URL

    # Переход "Конструктор"
    def test_go_to_constructor(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellarBurgersTestData.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (StellarBurgersLocators.BURGER_TEXT)
            )
        )
        success_url = driver.current_url
        assert success_url == urls.MAIN_PAGE_URL

    # Переход логотип сайта
    def test_go_to_logo(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellarBurgersTestData.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (StellarBurgersLocators.BURGER_TEXT)
            )
        )
        success_url = driver.current_url
        assert success_url == urls.MAIN_PAGE_URL

