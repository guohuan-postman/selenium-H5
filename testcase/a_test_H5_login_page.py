from public.common import mytest, datainfo
from public.pages import H5_Login_page
import time
from public.common import publicfunction

from public.common import pyselenium

class Test_H5_login(mytest.MyTest):

    def test_Login(self):
        H5_index_page = H5_Login_page.move_phone_login_page(self.dr)
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

    def test_search_excel(self):
        pass
        '''
        #使用数据驱动,进行测试
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        for data in datas:
            self._search(data)
            
        '''





