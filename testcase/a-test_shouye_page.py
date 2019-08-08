import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from public.common.log import Log
from selenium import webdriver
import unittest
from public.handle.shouye_page_handle import Shouye_Handle
from time import sleep

class Test_Shouye_Page(unittest.TestCase):


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
        self.selenium_driver.get('http://192.168.0.120:30180/login?redirect=%2Fshopping_cart')
        self.selenium_driver.accept_next_alert = True
        sleep(1)
        self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/p[2]').click()  # 点击密码登录按钮
        sleep(1)
        self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/input[1]').send_keys(18911111111)  # 点击请输入手机号输入框
        sleep(1)
        self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/input[2]').send_keys(123456)  # 点击请输入密码
        sleep(1)
        self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/input[3]').click()  # 点击登录按钮
        self.shouye_H = Shouye_Handle(self.selenium_driver)

    def tearDown(self):
        time.sleep(1)
        self.logger = Log()
        self.selenium_driver.quit()
        self.logger.info('###############################  End  ###############################')

    def test_shouye_search_button(self):
        #判断首页搜索按钮是否可用
        self.shouye_H.to_search_product()
        time.sleep(3)
        sousuo_button_text = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/span').text
        time.sleep(3)
        self.assertEqual(sousuo_button_text,'搜索',msg='如果断言失败，证明没有找到搜索按钮，用例失败')

    def test_search_product(self):
        #判断是否搜索出了商品
        self.shouye_H.input_number_and_click_sousuo_button()
        time.sleep(3)
        product = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div/p[1]/span').text
        time.sleep(3)
        self.assertEqual(product,'氢溴酸右美沙芬颗粒',msg='如果断言失败，证明没有找到相应商品，搜索失败')

    def test_click_huayaoshengwu_button(self):
        #点击化药生物按钮
        self.shouye_H.huayaoshengwu_button_click()

    def test_click_huayaoshengwu_button_check_product(self):
        time.sleep(3)
        self.shouye_H.huayaoshengwu_button_click()
        time.sleep(4)
        # 检查是否有商品名称，如果有，证明数据加载出来了。如果没有，证明页面没有数据
        product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span')
        self.assertIsNotNone(product_name, msg='如果断言失败，证明页面没有商品名称字段。页面没有被加载出来。')

    def test_search_product_huayaoshengwu(self):

        self.shouye_H.huayaoshengwu_button_click()
        time.sleep(5)
        self.shouye_H.click_search_button_huayaoshengwu_page()
        time.sleep(50)
        #self.shouye_H.click_sousuoshangpin_page_button_handle()
        huayaoshengwu_search_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div/p[1]/span').text
        self.assertIsNotNone(huayaoshengwu_search_product_name, msg='如果用例失败，证明没有找到需要搜索到的商品名称,第一种原因是：网页没有加载出来；第二种是：搜索不可用')

    #页面滑动到全部特惠 按钮处
    def test_ActionChains_to_quanbutehui(self):
        # 滑动页面到某个元素
        width = self.selenium_driver.get_window_size()['width']
        height = self.selenium_driver.get_window_size()['height']

        # while循环10次
        i = 0
        while i < 10:
            try:
                self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]')  # 尝试点击元素
                break
            except Exception as e:
                #self.selenium_driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)  # PC端页面滑动屏幕，H5和App没有swipe()方法
                start_button = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/ul/li[4]/img')
                time.sleep(3)
                Action = TouchActions(self.selenium_driver)

                """从 start_button 元素像下滑动200元素"""

                Action.scroll_from_element(start_button, width/2, height/2).perform()

                time.sleep(3)

                i = i + 1

            self.shouye_H.click_find_to_alltehui_Handle()
            # 特惠商品详情页，定位商品 维生素B12片  25ug*100s
            tehui_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/ul/li[4]/div/p[1]/span')
            self.assertEqual(tehui_product_name,'多维元素片21  复方*50片',msg='如果断言失败，证明没有找到这个商品。')

    #点击中药成分按钮
    def test_zhongyaochengfen_button(self):
        self.shouye_H.click_zhongyaochengfen_button_handle()
        time.sleep(3)
        zhongyaochengfen_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span').text
        self.assertIsNotNone(zhongyaochengfen_name,msg='断言中药成分的商品名称是否存在，如果断言失败，证明商品列表没有加载出来')

    #点击中药滋补按钮
    def test_click_zhongyaozibu_button(self):
        self.shouye_H.click_zhongyaozibu_button_handle()
        time.sleep(3)
        zhongyaozibu_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span').text
        self.assertIsNotNone(zhongyaozibu_product_name,msg='断言中药滋补的商品名称是否存在，如果断言失败，证明没有找到中药滋补的商品列表')

    #点击医疗器械按钮
    def test_click_yiliaoqixie_button(self):
        self.shouye_H.click_yiliaoqixie_button_handle()
        time.sleep(3)
        yiliaoqixie_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span').text
        self.assertIsNotNone(yiliaoqixie_product_name,msg='断言医疗器械的商品名称是否存在，如果断言失败，证明没有找到医疗器械商品列表')

    #点击计生用品按钮
    def test_click_jishengyongpin_button(self):
        self.shouye_H.click_jishengyongpin_button_handle()
        time.sleep(3)
        jishengyongpin_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span')
        self.assertIsNotNone(jishengyongpin_product_name,msg='断言计生用品的商品名称是否存在，如果断言失败，证明没有找到计生用品商品列表')

    # 点击医疗用品
    def test_click_yiliaoyongpin_button(self):
        self.shouye_H.click_yiliaoyongpin_button_handle()
        time.sleep(3)
        yiliaoyongpin_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span')
        self.assertIsNotNone(yiliaoyongpin_product_name,msg='断言医疗用品的商品名称是否存在，如果断言失败，证明没有找到医疗用品商品列表')

    # 点击养生保健
    def test_click_yangshengbaojian_button(self):
        self.shouye_H.click_yangshengbaojian_button_handle()
        time.sleep(3)
        yangshengbaojian_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span')
        self.assertIsNotNone(yangshengbaojian_product_name,msg='断言养生保健的商品名称是否存在，如果断言失败，证明没有找到养生保健商品列表')

    # 点击美妆百货
    def test_click_meizhuangbaihuo_button(self):
        self.shouye_H.click_meizhuangbaihuo_button_handle()
        time.sleep(3)
        meizhuangbaihuo_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span')
        self.assertIsNotNone(meizhuangbaihuo_product_name,msg='断言美妆百货的商品名称是否存在，如果断言失败，证明没有找到美妆百货商品列表')












