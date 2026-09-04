from pages.login_page import LoginPage


def test_valid_login_redirects_to_inventory(login_page: LoginPage):
    """测试场景：标准用户登录成功后，URL包含inventory"""
    login_page.login("standard_user", "secret_sauce")

    login_page.logger.info("📍 校验登录后URL")
    assert "inventory" in login_page.page.url, "登录后未跳转到商品页"

    login_page.assert_visible(".app_logo", message="校验App Logo出现")
