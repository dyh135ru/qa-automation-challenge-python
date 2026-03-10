from pages.common.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator("[data-test='product_sort_container']")
        self.burger_menu = page.locator("#react-burger-menu-btn")

    def add_to_cart(self, product_name):
        logger.info(f"Adding to cart: {product_name}")
        # Buscamos el botón 'Add to cart' que está en el mismo contenedor que el nombre del producto
        button_id = product_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='add-to-cart-{button_id}']").click()

    def remove_from_cart(self, product_name):
        logger.info(f"Removing from cart: {product_name}")
        button_id = product_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='remove-{button_id}']").click()

    def go_to_cart(self):
        logger.info("Opening shopping cart")
        self.cart_link.click()
