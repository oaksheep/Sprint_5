import urls
from locators import StellarBurgersLocators


class TestStellarBurgersEnterFromRegistrationForm:

    def test_enter_from_registration_form(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_IN_REGISTRATION_FORM).click()
        success_url = driver.current_url
        assert success_url == urls.ENTER_PAGE_URL
