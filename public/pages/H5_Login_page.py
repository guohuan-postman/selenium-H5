from public.common.basepage import Page
from public.common import pyselenium


class move_phone_login_page(Page):

    def __init__(self):
        pyselenium()

    def Open_login_page(self):
        '''打开H5首页'''
        self.dr.open('http://192.168.0.120:30080/')

    def click_buycar_to_login_page(self):
        '''点击购物车跳转到登入页'''
        self.dr.click('xpath->//*[@id="app"]/div/div[8]/ul/li[2]/a')

    def click_to_password_login_method(self):
        # 跳转到密码登入的方法
        self.dr.click('xpath->//*[@id="app"]/div/div[2]/div[1]/p[2]')


    def input_username(self):
        # 输入账号
        self.dr.type('xpath->//*[@id="app"]/div/div[2]/form[2]/input[1]', 15110048200)

    def input_password(self):
        # 输入密码
        self.dr.type('xpath->//*[@id="app"]/div/div[2]/form[2]/input[2]', 123456)

    def click_login_button(self):
        # 点击登入按钮
        self.dr.click('xpath->//*[@id="app"]/div/div[2]/form[2]/input[3]')









