from pages.base_page import BasePage

class LoginPage(BasePage):
    # 定位器
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test='error']"

    def login(self, username, password):
        self.logger.info(f"🔐 执行登录操作，账号: {username}")
        self.fill(self.USERNAME_INPUT, username, description="输入用户名")
        self.fill(self.PASSWORD_INPUT, password, description="输入密码")
        self.click(self.LOGIN_BTN, description="点击登录按钮")
        self.page.wait_for_load_state("networkidle")

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)