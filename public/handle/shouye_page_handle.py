from public.pages.shouye_page import ShouYe_Page
import time

class Shouye_Handle(object):
    def __init__(self,selenium_driver):
        self.shouye_P = ShouYe_Page(selenium_driver)

    def to_search_product(self):
        #点击首页搜索框，进入搜索页面
        self.shouye_P.click_to_search_product_page()



    def input_number_and_click_sousuo_button(self):
        #点击搜索框，输入商品编号
        self.shouye_P.click_to_search_product_page()
        self.shouye_P.click_input_number_product()
        self.shouye_P.click_input_number_product()
        self.shouye_P.input_number_product()
        self.shouye_P.click_sousuo_button()

    def huayaoshengwu_button_click(self):
        #点击化药生物图标
        self.shouye_P.click_huayaoshengwu_button()

    # 点击化药生物图标后，点击搜索也，输入商品编号,输入商品编号后，点击搜索按钮，查看是否搜索出来了商品名称
    def click_search_button_huayaoshengwu_page(self):
        self.shouye_P.click_search_button_search_product()
        self.shouye_P.input_product_num_66671()
        self.shouye_P.click_sousuoshangpin_page_button()


    def click_find_to_alltehui_Handle(self):
        self.shouye_P.click_find_to_alltehui()
    #点击中药成分按钮
    def click_zhongyaochengfen_button_handle(self):
        self.shouye_P.click_zhongyaochengfen_button()
    #点击中药滋补按钮
    def click_zhongyaozibu_button_handle(self):
        self.shouye_P.click_zhongyaozibu_button()

    #点击医疗器械按钮
    def click_yiliaoqixie_button_handle(self):
        self.shouye_P.click_yiliaoqixie_button()

    # 点击计生用品按钮
    def click_jishengyongpin_button_handle(self):
        self.shouye_P.click_jishengyongpin_button()

    # 点击医疗用品
    def click_yiliaoyongpin_button_handle(self):
        self.shouye_P.click_yiliaoyongpin_button()

    # 点击养生保健
    def click_yangshengbaojian_button_handle(self):
        self.shouye_P.click_yangshengbaojian_button()

    # 点击美妆百货
    def click_meizhuangbaihuo_button_handle(self):
        self.shouye_P.click_meizhuangbaihuo_button()


