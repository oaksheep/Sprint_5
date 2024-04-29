from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import StellarBurgersTestData
from locators import StellarBurgersLocators
import urls

class TestStellarBurgersExitFromAccount:

    def test_exit_from_account(self, driver):
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
        driver.find_element(*StellarBurgersLocators.EXIT_PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (StellarBurgersLocators.LOGIN_BUTTON)
            )
        )
        success_url = driver.current_url
        assert success_url == urls.ENTER_PAGE_URL
