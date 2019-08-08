import unittest
from public.handle.login_shouye_handle import Login_shouye_Handle
from public.common.log import Log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
        self.selenium_driver.get('https://release.yaodouwang.com')
        self.selenium_driver.accept_next_alert = True
        #等待点击购物车按钮
        WebDriverWait(self.selenium_driver, 10, 1).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[12]/ul/li[2]/a')))
        self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[12]/ul/li[2]/a').click()
        # 等待点击密码登入按钮
        WebDriverWait(self.selenium_driver, 10, 1).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/p[2]')))
        self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/p[2]').click()
        # 等待输入账号
        WebDriverWait(self.selenium_driver, 10, 1).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/form[2]/input[1]')))
        self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/input[1]').send_keys(18911111111)
        # 等待输入密码
        WebDriverWait(self.selenium_driver, 10, 1).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/form[2]/input[2]')))
        self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/input[2]').send_keys(123456)
        # 等待点击登入按钮
        WebDriverWait(self.selenium_driver, 10, 1).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/form[2]/input[3]')))
        self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/input[3]').click()
        time.sleep(3)

        #实例化handle类
        self.login_s_h = Login_shouye_Handle(self.selenium_driver)


    def tearDown(self):

        self.logger = Log()
        self.selenium_driver.quit()
        self.logger.info('###############################  End  ###############################')

    #检查登入后的首页搜索框
    def test_login_shouye_sousuo_button(self):
        self.login_s_h.click_login_shouye_sousuo_button_handle()
        # 定位搜索  商品页面 搜索框 ，输入  商品ID  E124222
        self.login_s_h.input_product_name_handle()
        # 定位 搜索按钮，点击搜索，查看是否搜索出来了商品
        self.login_s_h.sousuo_button_click_handle()
        time.sleep(3)
        # 查看搜索到的商品名称 是否是 蒲地蓝消炎片
        pudilanxiaoyanpian = self.login_s_h.check_product_name_pudilanxiaoyanpian_handle()
        self.assertEqual(pudilanxiaoyanpian,'蒲地蓝消炎片',msg='如果断言失败，证明没有找到次商品的名称，请检查首页的搜索功能是否可用')

    #查看华药生物分类页面是否有商品展示出来，
    def test_check_huayaoshengwu_product_show(self):
        #点击华药生物分类按钮
        self.login_s_h.check_huayaoshengwu_product_show_handle()
        #返回分类页面的第一个商品的名称  儿童麦冬灯芯花
        ertongmaidongdengxinhua = self.login_s_h.check_product_name_ertongmddxh_handle()
        self.assertEqual(ertongmaidongdengxinhua,'儿童麦冬灯芯花',msg='如果用例失败证明没有找到商品名称，请检查分类的详情页是否有商品展示出来')
        # 点击华药生物 搜索框，输入商品ID ： 99439，
        self.login_s_h.click_fenlei_sousuokuang_handle()
        # 点击分类搜索的  搜索 按钮
        self.login_s_h.click_fenlei_sousuo_button_handle()
        time.sleep(3)




