import pytest
import logging
from pytest_bdd import scenarios, given, when, then, parsers
from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.checkout_page import CheckoutPage
from playwright.sync_api import expect

# Configuración de Logging
logger = logging.getLogger(__name__)

# Vincular todos los archivos feature de SauceDemo
scenarios('../features/saucedemo/login.feature')
scenarios('../features/saucedemo/cart_management.feature')
scenarios('../features/saucedemo/checkout.feature')
scenarios('../features/saucedemo/responsive.feature')

# --- SHARED GIVEN STEPS ---

@given("the user is on the SauceDemo login page")
def open_login_page(page):
    login_pg = LoginPage(page)
    login_pg.navigate()

@given(parsers.parse('the user is logged into SauceDemo with "{user}"'))
def login_as_user(page, user):
    login_pg = LoginPage(page)
    login_pg.navigate()
    login_pg.login(user, "secret_sauce")

@given(parsers.parse('the user has "{product_name}" in the cart'))
def add_initial_product(page, product_name):
    # Reutilizamos el login estándar para pre-condiciones
    login_as_user(page, "standard_user")
    inv_pg = InventoryPage(page)
    inv_pg.add_to_cart(product_name)

# --- LOGIN STEPS ---

@when(parsers.parse('the user enters username "{user}" and password "{pwd}"'))
def step_login(page, user, pwd):
    login_pg = LoginPage(page)
    login_pg.login(user, pwd)

@then("the user should be redirected to the inventory page")
def verify_inventory_url(page):
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html") 

@then(parsers.parse('the product title "{title}" should be visible'))
def verify_title(page, title):
    inv_pg = InventoryPage(page)
    expect(inv_pg.title).to_have_text(title)

@then(parsers.parse('an error message "{message}" should be displayed'))
def verify_error_msg(page, message):
    login_pg = LoginPage(page)
    expect(login_pg.error_message).to_contain_text(message)

# --- CART STEPS ---

@when(parsers.parse('the user adds "{product_name}" to the cart'))
def add_product(page, product_name):
    inv_pg = InventoryPage(page)
    inv_pg.add_to_cart(product_name)

@then(parsers.parse('the cart badge should display "{count}"'))
def verify_cart_count(page, count):
    inv_pg = InventoryPage(page)
    expect(inv_pg.cart_badge).to_have_text(count)

@when(parsers.parse('the user removes "{product_name}" from the inventory page'))
def remove_product(page, product_name):
    inv_pg = InventoryPage(page)
    inv_pg.remove_from_cart(product_name)

@then("the cart badge should be empty")
def verify_empty_cart(page):
    inv_pg = InventoryPage(page)
    expect(inv_pg.cart_badge).not_to_be_visible()

# --- CHECKOUT STEPS ---

@given("the user has items in the shopping cart")
def prepare_cart_for_checkout(page):
    login_as_user(page, "standard_user")
    inv_pg = InventoryPage(page)
    inv_pg.add_to_cart("Sauce Labs Backpack")

@when("the user proceeds to checkout")
def go_to_checkout(page):
    inv_pg = InventoryPage(page)
    inv_pg.go_to_cart()
    page.locator("[data-test='checkout']").click()

@when(parsers.parse('fills the information with "{first}", "{last}", "{zip_code}"'))
def fill_checkout_info(page, first, last, zip_code):
    checkout_pg = CheckoutPage(page)
    checkout_pg.fill_information(first, last, zip_code)

@when("confirms the order summary")
def confirm_order(page):
    checkout_pg = CheckoutPage(page)
    checkout_pg.finish_checkout()

@then(parsers.parse('the order should be completed with message "{msg}"'))
def verify_completion(page, msg):
    checkout_pg = CheckoutPage(page)
    expect(checkout_pg.complete_header).to_have_text(msg)

@when("clicks continue without entering information")
def click_continue_empty(page):
    checkout_pg = CheckoutPage(page)
    checkout_pg.continue_btn.click()

# --- RESPONSIVE STEPS ---

@given("the user is on the SauceDemo login page with mobile viewport")
def open_login_mobile(page):
    # Playwright manejará el viewport automáticamente si el test tiene el tag @mobile
    # a través de la configuración que pusimos en conftest.py
    open_login_page(page)

@then("the side menu button should be visible")
def verify_burger_menu(page):
    inv_pg = InventoryPage(page)
    expect(inv_pg.burger_menu).to_be_visible()

@then("the inventory layout should adapt to mobile width")
def verify_mobile_layout(page):
    inv_pg = InventoryPage(page)
    logger.info("Verifying mobile layout adaptation")
    # En mobile, el contenedor de productos cambia de grid a lista simple
    # Validamos que el contenedor principal sea visible y responsivo
    expect(page.locator(".inventory_list")).to_be_visible()
    
    # Senior Tip: Validamos el ancho del viewport para confirmar que Playwright aplicó el resize
    viewport_size = page.viewport_size
    logger.info(f"Current viewport width: {viewport_size['width']}px")
    assert viewport_size['width'] == 375

@when(parsers.parse('the user logs in as "{user}"'))
def step_login_quick(page, user):
    from pages.saucedemo.login_page import LoginPage
    login_pg = LoginPage(page)
    # SauceDemo siempre usa 'secret_sauce' para sus usuarios de prueba
    logger.info(f"Quick login for mobile: {user}")
    login_pg.login(user, "secret_sauce")