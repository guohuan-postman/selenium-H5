
from public.pages.weidengru_index_page import Weidengru_index_page
import time

class Weidengru_index_page_handle(object):

    def __init__(self, selenium_driver):
        self.weidr = Weidengru_index_page(selenium_driver)
    #首页的搜索框搜索商品
    def shouye_sousuokuang_handle(self):
        # 点击 搜索商品名  搜索框
        self.weidr.shouye_sousuokuang().click()
        time.sleep(1)
        # 定位到 搜搜商品页面  搜索框
        self.weidr.click_sousuoshangpin_sousuokuang().click()
        time.sleep(1)
        #  搜索商品名  搜索框  中输入 商品编号
        self.weidr.sousuoshangpin_input_number()
        time.sleep(3)
        #点击 搜索 按钮
        self.weidr.click_sousuo_button().click()


    # 点击 华药生物 按钮,进入华药生物分类页面
    def go_to_huayaoshengwu_button_handle(self):
        #点击华药生物 按钮
        self.weidr.go_to_huayaoshengwu_button().click()

    #搜索华药生物搜索框的商品信息
    def sousuo_huayaoshengwu_product(self):
        # 定位 华药生物  搜索框
        self.weidr.go_to_huayaoshengwu_sousuokuang()
        # 点击 华药生物  搜索框  搜索按钮
        self.weidr.go_to_huayaoshengwu_sousuo_button().click()

    '''
        下面区域是推荐位管理区域
    '''
    #查看 首页 导航栏中  新客推荐栏  是否有商品展示
    def xin_ke_tui_jian_product_zhanshi_handle(self):
        return self.weidr.xin_ke_tui_jian_product_zhanshi()

    # 点击新客推荐更多  按钮，进入新客推荐列表详情页
    def go_to_xinketuijian_page_handle(self):
        self.weidr.go_to_xinketuijian_page().click()

    # 定位新客推荐列表详情页商品名称
    def check_xinketuijian_product_name_handle(self):
        return self.weidr.check_xinketuijian_product_name()

    # 页面滑动到 特价抢购 推荐位，
    def check_tejiaqianggou_page_handle(self):
        return self.weidr.check_tejiaqianggou_page()

    # 定位特价抢购 页面的商品名称
    def check_tejiaqianggou_product_name_handle(self):
        return self.weidr.check_tejiaqianggou_product_name()

    # 点击特价抢购  的  更多 按钮，进入 特价抢购商品列表详情页
    def find_tejiaqianggou_gengduo_button_handle(self):
       self.weidr.find_tejiaqianggou_gengduo_button().click()

    # 定位 特价抢购列表详情页的商品名称是否存在
    def check_tejiaqianggou_liebiao_handle(self):
        return self.weidr.check_tejiaqianggou_liebiao()

    # 返回特价抢购 商品列表页，商品是否有 会员可见 字样
    def check_tejiaqianggou_product_huiyuankejian_handle(self):
        return self.weidr.check_tejiaqianggou_product_huiyuankejian()

    '''
        通栏图片区域
    
    '''
    # 检查通栏图片是否有跳转链接,点击通栏图片进入活动专题页面
    def click_tonglantupian_handle(self):
        return self.weidr.click_tonglantupian().click()
    # 定位通栏图片的商品列表是否有商品名称
    def check_tonglantupian_product_list_handle(self):
        return self.weidr.check_tonglantupian_product_list()
    # 返回通栏图片的商品列表商品是否有 会员可见  字样
    def check_tonglantupian_product_huiyuankejian_handle(self):
        return self.weidr.check_tonglantupian_product_huiyuankejian()

    '''
      优惠商品推荐位
      '''

    # 查看首页优惠商品推荐位 是否有商品名称
    def youhuishangpin_product_name_handle(self):
        return self.weidr.youhuishangpin_product_name()

    # 返回首页优惠商品推荐位 商品有会员可见 字样
    def youhuishangpin_huiyuankejian_handle(self):
        return self.weidr.youhuishangpin_huiyuankejian()
    # 返回优惠商品 更多按钮，进入 优惠商品 列表详情页
    def youhuishangpin_product_list_handle(self):
        return self.weidr.youhuishangpin_product_list().click()

    # 返回优惠商品 列表详情页，是否有商品名称
    def youhuishangpin_product_name_handle(self):
        return self.weidr.youhuishangpin_product_name()

    # 返回优惠商品 列表详情页，商品是否有会员可见 字样
    def youhuishangpin_product_huiyuankejian_handle(self):
        return self.weidr.youhuishangpin_product_huiyuankejian()

    #返回首页  严选商品  商品名称
    def yanxuanshangpin_product_handle(self):
        return self.weidr.yanxuanshangpin_product()
    # 返回首页  严选商品  是否有 会员可见字样
    def yanxuanshangpin_huiyuankejian_handle(self):
        return self.weidr.yanxuanshangpin_huiyuankejian()

    # 定位首页  严选商品  点击更多按钮，进入 严选商品 列表详情页
    def yanxuanshangpin_product_list_handle(self):
        return self.weidr.yanxuanshangpin_product_list().click()

    # 返回，严选商品  商品详情页商品名称
    def yanxuanshangpin_find_product_name_handle(self):
        return self.weidr.yanxuanshangpin_find_product_name()
    # 返回，商品详情页是否有会员可见
    def yanxuanshangpin_find_huiyuankejian_handle(self):
        return self.weidr.yanxuanshangpin_find_huiyuankejian()

    '''
        旗舰店商家
    '''
    # 返回旗舰店商家 店铺名称
    def qijiandianshangjia_handle(self):
        return self.weidr.qijiandianshangjia()
    # 返回旗舰店商家 店铺是否有会员可见
    def qianjianguanshangjia_huiyuankejian_handle(self):
        return self.weidr.qianjianguanshangjia_huiyuankejian()
    # 旗舰店商家，点击 进店，进入店铺主页
    def qijianguan_jindian_handle(self):
        return self.weidr.qijianguan_jindian().click()
    # 返回店铺主页是否有商品名称
    def qijianguan_dianpu_product_lisr_handle(self):
        return self.weidr.qijianguan_dianpu_product_lisr()
    # 返回店铺主页是否有 会员可见
    def qijianguan_dianpu_huiyuankejian_handle(self):
        return self.weidr.qijianguan_dianpu_huiyuankejian()

    '''
        好货推荐
    '''
    #返回好货推荐商品名称
    def haohuotuijian_handle(self):
        return self.weidr.haohuotuijian()

    # 点击会员可见，页面跳转到 注册登入页面
    def click_huiyuankejian_to_login_handle(self):
        return self.weidr.click_huiyuankejian_to_login().click()

    # 返回 跳转页面是否有  验证码登入  字样
    def click_huiyuankejian_to_login_page_handle(self):
        return self.weidr.click_huiyuankejian_to_login_page()














