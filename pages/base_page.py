from playwright.sync_api import Page, expect
from config.settings import IMPLICIT_TIMEOUT
from utils.logger import get_logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()
        self.timeout = IMPLICIT_TIMEOUT

    def navigate(self, url):
        self.logger.info(f"🌐 导航至: {url}")
        self.page.goto(url)

    def click(self, selector, description=""):
        self.logger.info(f"🖱️ 点击元素: {selector} | 意图: {description}")
        self.page.locator(selector).click()

    def fill(self, selector, text, description=""):
        self.logger.info(f"⌨️ 输入框: {selector} | 输入值: {text} | 意图: {description}")
        self.page.locator(selector).fill(text)

    def get_text(self, selector):
        text = self.page.locator(selector).text_content()
        self.logger.debug(f"📄 获取文本: {selector} -> 返回: {text}")
        return text

    def take_screenshot(self, name="screenshot"):
        path = f"reports/screenshots/{name}.png"
        self.page.screenshot(path=path, full_page=True)
        self.logger.info(f"📸 截图已保存: {path}")
        return path

    def assert_visible(self, selector, message="元素可见性校验"):
        self.logger.info(f"✅ 断言可见: {selector} | {message}")
        expect(self.page.locator(selector)).to_be_visible()