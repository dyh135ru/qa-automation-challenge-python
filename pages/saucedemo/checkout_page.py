from pages.common.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Step 1: Information
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.zip_code = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")
        self.error_msg = page.locator("[data-test='error']")
        
        # Step 2: Overview & Finish
        self.finish_btn = page.locator("[data-test='finish']")
        self.complete_header = page.locator(".complete-header")

    def fill_information(self, first, last, zip_pt):
        logger.info(f"Filling checkout info for: {first} {last}")
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zip_code.fill(zip_pt)
        self.continue_btn.click()

    def finish_checkout(self):
        logger.info("Finishing checkout process")
        self.finish_btn.click()
