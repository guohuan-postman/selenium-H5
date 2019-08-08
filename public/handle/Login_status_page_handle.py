
from public.pages.Login_status_page import login_status_P

class login_status_page_H(object):
    def __init__(self, selenium_driver):
        self.login_h = login_status_P(selenium_driver)

    # 点击购物车按钮，进入登入页面
    def click_buycar_to_login_page_handle(self):
        return self.login_h.click_buycar_to_login_page().click()

    # 返回登入页面的  发送验证码 字样
    def fasongyanzhengma_text_handle(self):
        return self.login_h.fasongyanzhengma_text()

    # 登入页面，点击密码登入按钮，进入密码登入页面
    def click_mimadengru_button_handle(self):
        return self.login_h.click_mimadengru_button().click()

    # 定位到 忘记密码字样
    def wangjimima_text_handle(self):
        return self.login_h.wangjimima_text()

    '''
        密码登入页面，输入账号密码，点击登入，
    '''
    def click_dengru_to_shouye_handle(self):
        self.login_h.input_phone()
        self.login_h.input_mima()
        self.login_h.click_dengru_button().click()

    # 登入后，查看是否有 757+  药房
    def yaofang_text_handle(self):
        return self.login_h.yaofang_text()

