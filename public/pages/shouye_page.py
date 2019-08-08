from public.pages.base_page import Base_Page

class ShouYe_Page(object):
    def __init__(self,selenium_driver):
        self.Base_P = Base_Page(selenium_driver)

    def click_to_search_product_page(self):
        #点击去搜索商品页面
        return self.Base_P.click('xpath->//*[@id="app"]/div/div[1]/div[1]/p')


    def click_input_number_product(self):
        #点击输入框
        return self.Base_P.click('xpath->//*[@id="app"]/div/div[1]/div[2]/input')

    def input_number_product(self):
        #输入商品编号
        return self.Base_P.type('xpath->//*[@id="app"]/div/div[1]/div[2]/input', 98144)

    def click_sousuo_button(self):
        #点击搜索按钮
        return self.Base_P.click('xpath->//*[@id="app"]/div/div[1]/div[2]/span')

    def click_huayaoshengwu_button(self):
        #点击化药生物按钮

        return self.Base_P.click('xpath->//*[@id="app"]/div/div[2]/ul/li[1]/img')

    def click_search_button_search_product(self):
        return self.Base_P.click('xpath->//*[@id="app"]/div/div/div[2]/div[1]/div[1]/input')
        # 点击化药生物搜索框，搜索产品

    def input_product_num_66671(self):
        # 搜索框输入 66671 这个商品编号
        return self.Base_P.type('xpath->//*[@id="app"]/div/div[1]/div[2]/input', 66671)

    # 输入商品名称后，点击搜索按钮
    def click_sousuoshangpin_page_button(self):
        return self.Base_P.click('xpath->//*[@id="app"]/div/div[1]/div[2]/span')

    #点击全部特惠按钮，进入全部特惠详情页面
    def click_find_to_alltehui(self):
        self.Base_P.click('xpath->//*[@id="app"]/div/div[4]/div/div[2]')

    #特惠商品详情页，定位商品 维生素B12片  25ug*100s
    def find_product_(self):
        self.Base_P.get_element('xpath->//*[@id="app"]/div/div[2]/ul/li[4]/div/p[1]/span')
    #点击中药成分按钮
    def click_zhongyaochengfen_button(self):
        self.Base_P.click('xpath->//*[@id="app"]/div/div[2]/ul/li[2]/img')

    #点击中药滋补 按钮
    def click_zhongyaozibu_button(self):
        self.Base_P.click('xpath->//*[@id="app"]/div/div[2]/ul/li[3]/img')

    #点击医疗器械按钮
    def click_yiliaoqixie_button(self):
        self.Base_P.click('xpath->//*[@id="app"]/div/div[2]/ul/li[4]/img')

    #点击计生用品按钮
    def click_jishengyongpin_button(self):
        self.Base_P.click('xpath->//*[@id="app"]/div/div[2]/ul/li[5]/img')

    #点击医疗用品
    def click_yiliaoyongpin_button(self):
        self.Base_P.click('xpath->//*[@id="app"]/div/div[2]/ul/li[6]/img')

    #点击养生保健
    def click_yangshengbaojian_button(self):
        self.Base_P.click('xpath->//*[@id="app"]/div/div[2]/ul/li[7]/img')

    # 点击美妆百货
    def click_meizhuangbaihuo_button(self):
        self.Base_P.click('xpath->//*[@id="app"]/div/div[2]/ul/li[8]/img')














