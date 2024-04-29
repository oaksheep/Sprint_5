from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
from data import StellarBurgersTestData

class TestStellarBurgersIngredientsTabs:

    # Таб "Соусы"
    def test_sauces_tab(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellarBurgersTestData.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (StellarBurgersLocators.SAUCES_LOCATION_BUTTON)
            )
        )
        driver.find_element(*StellarBurgersLocators.SAUCES_LOCATION_BUTTON).click()
        sauces_class_parent = driver.find_element(*StellarBurgersLocators.SAUCES_PARRENT_CLASS)
        success_class = driver.find_element(*StellarBurgersLocators.CURRENT_SECTION)
        assert success_class == sauces_class_parent

    # Таб "Начинки"
    def test_fillings_tab(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellarBurgersTestData.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (StellarBurgersLocators.FILLINGS_LOCATION_BUTTON)
            )
        )
        driver.find_element(*StellarBurgersLocators.FILLINGS_LOCATION_BUTTON).click()
        fillings_class_parent = driver.find_element(*StellarBurgersLocators.FILLINGS_PARRENT_CLASS)
        success_class = driver.find_element(*StellarBurgersLocators.CURRENT_SECTION)
        assert success_class == fillings_class_parent

    # Таб "Булки"
    def test_buns_tab(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellarBurgersTestData.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (StellarBurgersLocators.FILLINGS_LOCATION_BUTTON)
            )
        )
        driver.find_element(*StellarBurgersLocators.FILLINGS_LOCATION_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.BUNS_LOCATION_BUTTON).click()
        buns_class_parent = driver.find_element(*StellarBurgersLocators.BUNS_PARRENT_CLASS)
        success_class = driver.find_element(*StellarBurgersLocators.CURRENT_SECTION)
        assert success_class == buns_class_parent
