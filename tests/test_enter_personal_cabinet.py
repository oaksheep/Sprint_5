import urls
from locators import StellarBurgersLocators

class TestStellarBurgersEnterPersonalCabinet:

    def test_enter_personal_cabinet(self, driver):
        driver.find_element(*StellarBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        success_url = driver.current_url
        assert success_url == urls.ENTER_PAGE_URL
