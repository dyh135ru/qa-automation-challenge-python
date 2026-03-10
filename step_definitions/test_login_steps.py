import os
import logging
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from playwright.sync_api import expect

logger = logging.getLogger(__name__)
scenarios('../features/login.feature')

@given("the user is on the login page")
def step_open_login(page):
    login_pg = LoginPage(page)
    logger.info("Navigating to Login Page")
    login_pg.navigate("/login")

@when(parsers.parse('the user enters username "{username}" and password "{password}"'))
def step_do_login(page, username, password):
    login_pg = LoginPage(page)
    login_pg.login(username, password)

@then(parsers.parse('the system should display the message "{expected_message}"'))
def step_verify_message(page, expected_message):
    login_pg = LoginPage(page)
    logger.info(f"Verifying flash message contains: {expected_message}")
    expect(login_pg.flash_message).to_contain_text(expected_message)
