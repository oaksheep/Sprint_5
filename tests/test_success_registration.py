from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators
from faker import Faker
import urls


fake = Faker()
class TestStellarBurgersRegistration:

    def test_success_registration(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_INPUT).send_keys(fake.name())
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_INPUT).send_keys(fake.email())
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_INPUT).send_keys(fake.password())
        driver.find_element(*StellarBurgersLocators.CONFIRM_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located
            ((StellarBurgersLocators.LOGIN_BUTTON))
        )
        url_validation = driver.current_url
        assert urls.REGISTRATION_SUCCES_URL == url_validation
