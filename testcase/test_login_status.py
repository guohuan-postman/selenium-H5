import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from public.handle.Login_status_page_handle import login_status_page_H
from public.common.log import Log
from selenium import webdriver

import time
class Login_status(unittest.TestCase):

    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        WIDTH = 375
        HEIGHT = 812
        PIXEL_RATIO = 3.0
        UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                           "userAgent": UA}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.selenium_driver = webdriver.Chrome(options=chrome_options)  # 移动端配置
        self.selenium_driver.maximize_window()
        self.selenium_driver.get('http://192.168.0.120:30180')
        self.selenium_driver.accept_next_alert = True
        #self.weidengru_handle = Weidengru_index_page_handle(self.selenium_driver)
        self.login_status_H = login_status_page_H(self.selenium_driver)

    def tearDown(self):

        self.logger = Log()
        self.selenium_driver.quit()
        self.logger.info('###############################  End  ###############################')

    # 点击购物车按钮，进入登入页面
    def test_click_buycar_to_login_page_handle(self):
        self.login_status_H.click_buycar_to_login_page_handle()
        time.sleep(3)
        dengru_page_fasongyanzhengma = self.login_status_H.fasongyanzhengma_text_handle()
        self.assertEqual(dengru_page_fasongyanzhengma,'发送验证码',msg='如果断言失败，证明没有找到 发送验证码，字样，请检查，点击 购物车 进入登入页面时，是否页面可跳转')

    # 登入页面，点击密码登入按钮，进入密码登入页面
    def test_click_mimadengru_button(self):
        # 点击购物车按钮，进入登入页面
        self.login_status_H.click_buycar_to_login_page_handle()
        # 登入页面，点击密码登入按钮，进入密码登入页面
        self.login_status_H.click_mimadengru_button_handle()
        mimadengru_wangjimima = self.login_status_H.wangjimima_text_handle()
        self.assertEqual(mimadengru_wangjimima, '忘记密码 ?', msg='如果断言失败，证明没有找到 忘记密码，字样，请检查，点击 购物车 进入登入页面后，点击密码登入，查看是否页面可跳转')
        time.sleep(3)

    #输入账号密码，点击登入，查看页面是否跳转成功   (登入的主要方法)
    def test_click_dengru_to_shouye(self):
        # 点击购物车按钮，进入登入页面
        self.login_status_H.click_buycar_to_login_page_handle()
        # 登入页面，点击密码登入按钮，进入密码登入页面
        self.login_status_H.click_mimadengru_button_handle()
        #输入账号密码
        self.login_status_H.click_dengru_to_shouye_handle()
        #点击登入按钮

        #获取化药生物的  分类的  文字
        huayaosw_text = self.login_status_H.yaofang_text_handle()
        self.assertEqual(huayaosw_text, '药房', msg='如果断言失败，证明没有找到华药生物的分类的 文字，请检查，登入功能是否可用')







