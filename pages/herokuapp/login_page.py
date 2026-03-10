import os
import logging
from pages.common.base_page import BasePage 
logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators específicos de Herokuapp
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def navigate(self, endpoint):
        import os
        base_url = os.getenv("BASE_URL")
        target_url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        super().navigate(target_url)

    def login(self, user, pwd):
        logger.info(f"Attempting login for user: {user}")
        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_button.click()
        logger.info("Login button clicked")
