from public.pages.base_page import Base_Page

class Login_Shouye(object):
    def __init__(self,selenium_driver):
        self.base_P = Base_Page(selenium_driver)
    #点击登入 后的首页的搜索框 按钮
    def click_login_shouye_sousuo_button(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[1]/div[1]/p')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[1]/div[1]/p')

    #定位搜索  商品页面 搜索框 ，输入  商品ID  158175
    def input_product_name(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[1]/div[2]/input')
        return self.base_P.type('xpath->//*[@id="app"]/div/div[1]/div[2]/input', 'E124222')
    #定位 搜索按钮，点击搜索，查看是否搜索出来了商品
    def sousuo_button_click(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[1]/div[2]/span')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[1]/div[2]/span')
    #查看搜索到的商品名称 是否是 蒲地蓝消炎片
    def check_product_name_pudilanxiaoyanpian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div/p[1]/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div/p[1]/span')
    '''
    查看华药生物分类页面是否有商品展示出来，
    '''
    #点击华药生物按钮
    def check_huayaoshengwu_product_show(self):
        # 点击华药生物按钮
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[3]/ul/li[1]')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[3]/ul/li[1]')
    #查看显示出来的商品名称是不是 儿童麦冬灯芯花
    def check_product_name_ertongmddxh(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]/span')
    #点击华药生物 搜索框，输入商品ID ： 99439，
    def click_fenlei_sousuokuang(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div/div[2]/div[1]/div[1]/input')
        return self.base_P.type('xpath->//*[@id="app"]/div/div/div[2]/div[1]/div[1]/input',99439)

    #点击分类搜索的  搜索 按钮
    def click_fenlei_sousuo_button_a(self):
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[1]/div[2]/span')
        #self.base_P.element_wait('xpath->//*[@id="app"]/div/div/div[2]/div[1]/div[1]/span')










