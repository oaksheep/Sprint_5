import urls
from locators import StellarBurgersLocators


class TestStellarBurgersEnterFromRestorePassword:

    def test_enter_from_restore_password(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.RESTORE_PASSWORD_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_IN_RESTORE_PASSWORD).click()
        success_url = driver.current_url
        assert success_url == urls.ENTER_PAGE_URL