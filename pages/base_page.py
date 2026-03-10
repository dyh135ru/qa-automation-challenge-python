import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del .env

class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")

    def navigate(self, endpoint):
        self.page.goto(f"{self.base_url}{endpoint}")
