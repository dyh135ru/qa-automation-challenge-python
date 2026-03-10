import os
import logging
from dotenv import load_dotenv
from playwright.sync_api import Page, Response

load_dotenv()
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> Response:
        """
        Navigates to a specific URL and logs the action.
        This works for both Herokuapp and SauceDemo.
        """
        logger.info(f"Navigating to: {url}")
        return self.page.goto(url)

    def get_title(self) -> str:
        """Returns the current page title."""
        return self.page.title()

    def wait_for_load_state(self, state: str = "networkidle"):
        """Waits for a specific network state (default: networkidle)."""
        self.page.wait_for_load_state(state)
