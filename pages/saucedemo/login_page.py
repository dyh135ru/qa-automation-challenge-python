import logging
from pages.common.base_page import BasePage

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # URL fija para SauceDemo (Producción/Testing)
        self.url = "https://www.saucedemo.com" 
        
        # Locators con data-test (Best practice para SauceDemo)
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        """Usa el método del padre para mantener consistencia en logs"""
        super().navigate(self.url)

    def login(self, user, pwd):
        logger.info(f"Attempting login for user: {user}")
        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_button.click()
        logger.info("Login button clicked")
