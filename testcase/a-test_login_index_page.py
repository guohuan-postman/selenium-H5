from public.common.log import Log
from selenium import webdriver
from public.handle.login_index_page_handle import Login_Index_Page_Handle
import time
import unittest

class Test_Login_Index_Page(unittest.TestCase):
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

        self.selenium_driver.get('http://192.168.0.120:30180/login?redirect=%2Fshopping_cart')
        self.login_I_p_H = Login_Index_Page_Handle(self.selenium_driver)



    def test_login_success_methon(self):
        self.login_I_p_H.login(18911111111,123456)
        ss = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/p/a')
        ss.text
        self.assertNotEqual(ss, '忘记密码 ?', msg='用例失败，证明登入不成功，找到了 忘记密码 ?')


    def test_login_error_method(self):
        self.login_I_p_H.login(15100000000,111111)
        ss1 = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/p/a').text
        self.assertEqual(ss1, '忘记密码 ?', msg='用例失败，证明登入不成功，找到了 忘记密码 ?')







    def tearDown(self):

        self.logger = Log()
        self.selenium_driver.quit()
        self.logger.info('###############################  End  ###############################')