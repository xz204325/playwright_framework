import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from config.settings import BASE_URL
from utils.logger import get_logger

# 固件：自动注入 page 对象，并设置视口大小
@pytest.fixture(scope="function")
def page(page: Page) -> Page:
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page

# 固件：直接返回已导航到登录页的 LoginPage 对象
@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.navigate(BASE_URL)
    return login

# ---------- 失败自动截图钩子（面试亮点） ----------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        logger = get_logger()
        if "page" in item.fixturenames:
            page = item.funcargs["page"]
            screenshot_path = f"reports/screenshots/{item.name}_失败截图.png"
            page.screenshot(path=screenshot_path, full_page=True)
            logger.error(f"❌ 用例 {item.name} 执行失败，截图已保存: {screenshot_path}")
        else:
            logger.error(f"❌ 用例 {item.name} 执行失败，但无法获取page对象截图")