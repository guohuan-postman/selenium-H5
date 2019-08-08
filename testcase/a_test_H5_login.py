import unittest
from public.common.log import Log
from config import globalparam
from public.common import pyselenium
from public.common import mytest, datainfo
from public.pages import H5_Login_page
import time
from public.pages.H5_search_product import Search_product

class Test_H5_Login(unittest.TestCase):


    def test_Login(self):
        H5_index_page = H5_Login_page.move_phone_login_page(self.setUp())
        H5_index_page.Open_login_page()
        time.sleep(2)
        H5_index_page.click_buycar_to_login_page() #点击购物车，去登入页
        time.sleep(2)
        H5_index_page.click_to_password_login_method()
        time.sleep(1)
        #now = time.strftime('%Y-%m-%d_%H_%M_%S')
        #publicfunction.get_img('登入后的首页'+ now + '.png')

        H5_index_page.input_username()
        time.sleep(1)

        H5_index_page.input_password()
        time.sleep(1)

        H5_index_page.click_login_button()

    def test_search_product(self):
        self.Search_Product = Search_product(self.dr)

        self.Search_Product.click_search_text()
        self.Search_Product.input_product_number()
        self.Search_Product.click_sousuo_button()
        time.sleep(5)
        product_name = self.Search_Product.product_name_test()

        self.assertEqual(product_name, '采森牌采森钙片（儿童型）', msg='没有查询到商品，或者商品不是采森牌采森钙片（儿童型）这个名称')