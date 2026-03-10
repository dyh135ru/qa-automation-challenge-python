import os
import logging
from pytest_bdd import scenarios, given, when, then, parsers
from pages.herokuapp.login_page import LoginPage
from pages.herokuapp.complex_pages import UploadPage, DynamicPage, DropdownPage
from playwright.sync_api import expect

logger = logging.getLogger(__name__)

scenarios('../features/herokuapp') 

# --- AUTHENTICATION STEPS ---

@given("the user is on the login page")
def step_open_login(page):
    login_pg = LoginPage(page)
    logger.info("Navigating to Herokuapp Login")
    login_pg.navigate("/login")

@when(parsers.parse('the user enters username "{username}" and password "{password}"'))
def step_do_login(page, username, password):
    login_pg = LoginPage(page)
    login_pg.login(username, password)

@then(parsers.parse('the system should display the message "{expected_message}"'))
def step_verify_login_msg(page, expected_message):
    login_pg = LoginPage(page)
    expect(login_pg.flash_message).to_contain_text(expected_message)

# --- FILE UPLOAD STEPS ---

@given("the user is on the file upload page")
def step_open_upload(page):
    upload_pg = UploadPage(page)
    upload_pg.navigate("/upload")

@when("the user uploads a test file")
def step_upload_file(page):
    upload_pg = UploadPage(page)
    file_name = "test_evidence.txt"
    file_path = os.path.abspath(file_name)
    
    with open(file_name, "w") as f:
        f.write("QA Automation Evidence")
    
    upload_pg.upload_file(file_path)

@then(parsers.parse('the system should display the "{msg}" confirmation message'))
def step_verify_upload(page, msg):
    expect(UploadPage(page).success_msg).to_have_text(msg)

# --- DYNAMIC LOADING STEPS ---

@given("the user is on the dynamic loading page")
def step_open_dynamic(page):
    DynamicPage(page).navigate("/dynamic_loading/1")

@when("the user clicks the start button")
def step_click_start(page):
    DynamicPage(page).start_loading()

@then(parsers.parse('the text "{expected_text}" should appear after loading'))
def step_verify_dynamic(page, expected_text):
    dynamic_pg = DynamicPage(page)
    # Senior timeout handling
    expect(dynamic_pg.finish_text).to_be_visible(timeout=10000)
    expect(dynamic_pg.finish_text).to_have_text(expected_text)

# --- DROPDOWN STEPS ---

@given("the user is on the dropdown page")
def step_open_dropdown(page):
    DropdownPage(page).navigate("/dropdown")

@when(parsers.parse('the user selects the option "{option_text}"'))
def step_select_dropdown(page, option_text):
    DropdownPage(page).select_option_by_label(option_text)

@then(parsers.parse('the selected value should be "{value}"'))
def step_verify_dropdown(page, value):
    expect(DropdownPage(page).select_element).to_have_value(value)
