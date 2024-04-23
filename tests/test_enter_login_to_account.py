import urls
from locators import StellarBurgersLocators

class TestStellarBurgersEnterLoginToAccount:

    def test_enter_login_to_account(self, driver):
        driver.find_element(*StellarBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        success_url = driver.current_url
        assert success_url == urls.ENTER_PAGE_URL
