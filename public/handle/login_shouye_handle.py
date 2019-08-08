from public.pages.login_shouye import Login_Shouye

class Login_shouye_Handle(object):
    def __init__(self,selenium_driver):
        self.login_S = Login_Shouye(selenium_driver)

    # 点击登入 后的首页的搜索框 按钮
    def click_login_shouye_sousuo_button_handle(self):
        self.login_S.click_login_shouye_sousuo_button().click()

    # 定位搜索  商品页面 搜索框 ，输入  商品ID  158175
    def input_product_name_handle(self):
        return self.login_S.input_product_name()

    # 定位 搜索按钮，点击搜索，查看是否搜索出来了商品
    def sousuo_button_click_handle(self):
        return self.login_S.sousuo_button_click().click()
    # 查看搜索到的商品名称 是否是 蒲地蓝消炎片
    def check_product_name_pudilanxiaoyanpian_handle(self):
        return self.login_S.check_product_name_pudilanxiaoyanpian()

    # 查看华药生物分类页面是否有商品展示出来，并点击
    def check_huayaoshengwu_product_show_handle(self):
        return self.login_S.check_huayaoshengwu_product_show().click()
    # 查看显示出来的商品名称是不是 儿童麦冬灯芯花
    def check_product_name_ertongmddxh_handle(self):
        return self.login_S.check_product_name_ertongmddxh()
    # 点击华药生物 搜索框，输入商品ID ： 99439，
    def click_fenlei_sousuokuang_handle(self):
        return self.login_S.click_fenlei_sousuokuang()
    # 点击分类搜索的  搜索 按钮
    def click_fenlei_sousuo_button_handle(self):

        return self.login_S.click_fenlei_sousuo_button_a().click()
