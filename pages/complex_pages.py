import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class UploadPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.file_input = page.locator("#file-upload")
        self.upload_btn = page.locator("#file-submit")
        self.success_msg = page.locator("h3")
        self.uploaded_files_list = page.locator("#uploaded-files")

    def upload_file(self, file_path):
        logger.info(f"Uploading file from path: {file_path}")
        self.file_input.set_input_files(file_path)
        self.upload_btn.click()
        logger.info("Upload button clicked")

class DynamicPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.start_btn = page.locator("#start button")
        self.finish_text = page.locator("#finish h4")
        self.loading_bar = page.locator("#loading")

    def start_loading(self):
        logger.info("Clicking the Start button for dynamic content")
        self.start_btn.click()

class DropdownPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.select_element = page.locator("#dropdown")

    def select_option_by_label(self, label):
        logger.info(f"Selecting dropdown option: {label}")
        self.select_element.select_option(label=label)
