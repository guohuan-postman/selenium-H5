from public.pages.base_page import Base_Page


class login_status_P(object):
    def __init__(self,selenium_driver):
        self.base_P = Base_Page(selenium_driver)
    #点击购物车按钮，进入登入页面
    def click_buycar_to_login_page(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[12]/ul/li[2]/a')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[12]/ul/li[2]/a')
    #定位登入页面的  发送验证码 字样
    def fasongyanzhengma_text(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/form[1]/div/button')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/form[1]/div/button')
    #登入页面，点击密码登入按钮，进入密码登入页面
    def click_mimadengru_button(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/div[1]/p[2]')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[2]/div[1]/p[2]')
    #定位到 忘记密码字样
    def wangjimima_text(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/form[2]/p/a')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/form[2]/p/a')
    '''
    密码登入页面，输入账号密码，点击登入，
    '''
    # 定位 到输入账号
    def input_phone(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/form[2]/input[1]')
        return self.base_P.type('xpath->//*[@id="app"]/div/div[2]/form[2]/input[1]',18911111111)

    #定位到输入密码
    def input_mima(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/form[2]/input[2]')
        return self.base_P.type('xpath->//*[@id="app"]/div/div[2]/form[2]/input[2]',123456)
    #定位到 登入  按钮
    def click_dengru_button(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/form[2]/input[3]')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[2]/form[2]/input[3]')

    #登入后，查看是否有 757+  药房
    def yaofang_text(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[1]/div[5]/ul/li[2]/span[2]')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[1]/div[5]/ul/li[2]/span[2]')



