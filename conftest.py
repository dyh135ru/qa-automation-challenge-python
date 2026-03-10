import pytest
import allure
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def page(browser):
    logger.info("--- Starting Test Execution ---")
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1280, "height": 720})
    yield page
    logger.info("--- Closing Browser Context ---")
    context.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        page = item.funcargs.get('page')
        if page:
            logger.error(f"Test Failed: {item.name}")
            allure.attach(
                page.screenshot(full_page=True),
                name="error_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
@pytest.fixture
def page(browser, request):
    viewport_config = {"width": 1280, "height": 800}
    
    if "mobile" in request.node.keywords:
        viewport_config = {"width": 375, "height": 667}
        logger.info("Setting viewport to Mobile (375x667) for this scenario")
    else:
        logger.info("Setting viewport to Desktop (1280x800)")

    context = browser.new_context(viewport=viewport_config)
    page = context.new_page()
    
    yield page
    
    context.close()
