from public.common import mytest
from public.pages.H5_search_product import Search_product
import time

from public.pages import H5_search_product
from public.pages.H5_search_product import Search_product


class Test_H5_Search_Product(mytest.MyTest):


    def test_search_product(self):
        self.Search_Product = Search_product(self.dr)
        self.Search_Product.click_search_text()
        self.Search_Product.input_product_number()
        self.Search_Product.click_sousuo_button()
        time.sleep(5)
        product_name = self.Search_Product.product_name_test()

        self.assertEqual(product_name, '采森牌采森钙片（儿童型）', msg='没有查询到商品，或者商品不是采森牌采森钙片（儿童型）这个名称')



'''
    def test_asser_product_name(self):

        product_name = self.H5_search.product_name_test()
        self.assertIn(product_name, '采森牌采森钙片（儿童型）', msg='没有查询到商品，或者商品不是采森牌采森钙片（儿童型）这个名称')
        self.dr.quit()

'''

