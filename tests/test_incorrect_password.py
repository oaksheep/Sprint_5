from locators import StellarBurgersLocators
from data import StellarBurgersTestData

class TestStellarBurgersIncorrectPassword:

    def test_incorrect_password(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_INPUT).send_keys(StellarBurgersTestData.NAME)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_INPUT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_INPUT).send_keys(StellarBurgersTestData.INCORRECT_PASSWORD)
        driver.find_element(*StellarBurgersLocators.CONFIRM_REGISTRATION_BUTTON).click()
        error = driver.find_element(*StellarBurgersLocators.INCORRECT_PASSWORD_TEXT).text
        assert error == "Некорректный пароль"
