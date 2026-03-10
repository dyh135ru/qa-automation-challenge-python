import os
import logging
from pytest_bdd import scenarios, given, when, then, parsers
from pages.complex_pages import UploadPage, DynamicPage, DropdownPage
from playwright.sync_api import expect

logger = logging.getLogger(__name__)

# Linking the feature files
scenarios('../features/upload.feature')
scenarios('../features/dynamic_loading.feature')
scenarios('../features/dropdown.feature')

# --- STEPS FOR THE FILE UPLOAD ---

@given("the user is on the file upload page")
def step_open_upload(page):
    upload_pg = UploadPage(page)
    logger.info("Navigating to File Upload module")
    upload_pg.navigate("/upload")

@when("the user uploads a test file")
def step_upload_file(page):
    upload_pg = UploadPage(page)
    
    file_name = "test_evidence.txt"
    file_path = os.path.abspath(file_name)
    
    with open(file_name, "w") as f:
        f.write("QA Automation Challenge Evidence")
    
    upload_pg.upload_file(file_path)

@then(parsers.parse('the system should display the "{expected_message}" confirmation message'))
def step_verify_upload_success(page, expected_message):
    upload_pg = UploadPage(page)
    logger.info(f"Verifying success message: {expected_message}")
    
    # Asserting the header text
    expect(upload_pg.success_msg).to_have_text(expected_message)
    # Also verifying the filename is listed
    expect(upload_pg.uploaded_files_list).to_contain_text("test_evidence.txt")
    logger.info("File upload successfully verified")

# --- STEPS FOR THE DYNAMIC LOADING ---

@given("the user is on the dynamic loading page")
def step_open_dynamic(page):
    dynamic_pg = DynamicPage(page)
    logger.info("Navigating to Dynamic Loading module")
    dynamic_pg.navigate("/dynamic_loading/1")

@when("the user clicks the start button")
def step_click_start(page):
    dynamic_pg = DynamicPage(page)
    dynamic_pg.start_loading()

@then(parsers.parse('the text "{expected_text}" should appear after loading'))
def step_verify_dynamic_text(page, expected_text):
    dynamic_pg = DynamicPage(page)
    logger.info(f"Waiting for text '{expected_text}' to become visible")
    
    expect(dynamic_pg.finish_text).to_be_visible(timeout=10000)
    expect(dynamic_pg.finish_text).to_have_text(expected_text)
    logger.info("Dynamic text successfully displayed")

# --- STEPS FOR THE DROPDOWN ---

@given("the user is on the dropdown page")
def open_dropdown(page):
    dropdown_pg = DropdownPage(page)
    logger.info("Navigating to Dropdown module")
    dropdown_pg.navigate("/dropdown")

@when(parsers.parse('the user selects the option "{option_text}"'))
def step_select_dropdown_option(page, option_text):
    dropdown_pg = DropdownPage(page)
    dropdown_pg.select_option_by_label(option_text)

@then(parsers.parse('the selected value should be "{value}"'))
def step_verify_dropdown_value(page, value):
    dropdown_pg = DropdownPage(page)
    logger.info(f"Verifying that the selected value is: {value}")
    expect(dropdown_pg.select_element).to_have_value(value)