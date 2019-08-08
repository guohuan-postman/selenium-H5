
import unittest
from public.common import pyselenium
from config import globalparam
from public.common.log import Log
from public.handle.login_handle import Login_Handle
from selenium import webdriver
import time
from public.pages.base_page import Base_Page

class Test_Login_Page(unittest.TestCase):

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
        self.selenium_driver.accept_next_alert = True
        #self.selenium_driver = webdriver.Chrome()
        self.selenium_driver.get('http://192.168.0.120:30180')
        time.sleep(3)
        self.Login_H = Login_Handle(self.selenium_driver)

    def tearDown(self):
        time.sleep(3)
        self.logger = Log()
        self.selenium_driver.quit()
        self.logger.info('###############################  End  ###############################')

    def test_click_buycar_to_login(self):
        #跳转到登入页面
        self.Login_H.click_to_login_page()

    def test_assert_no_buycar_wenzi(self):
        #self.assertNotIn('购物车', msg='页面跳转成功，没有找到 购物车 三个字')
        bugcar_wenzi = self.Login_H.find_buycar()
        #self.assertEqual('购物车',bugcar_wenzi,msg='页面跳转成功，没有找到 购物车 三个字')
        self.assertNotEqual('购物车',bugcar_wenzi,msg='页面跳转成功，没有找到 购物车 三个字')




