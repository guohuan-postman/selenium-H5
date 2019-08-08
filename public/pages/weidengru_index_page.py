from public.pages.base_page import Base_Page


class Weidengru_index_page(object):

    def __init__(self, selenium_driver):
        self.base_P = Base_Page(selenium_driver)

    #定位到 搜索商品名  搜索框
    def shouye_sousuokuang(self):
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[1]/div[1]/p')

    #点击搜索商品名搜索框后，进入搜索商品页面，点击搜索框
    def click_sousuoshangpin_sousuokuang(self):
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[1]/div[2]/input')

    #  搜索商品名  搜索框  中输入 商品编号
    def sousuoshangpin_input_number(self):
        return self.base_P.type('xpath->//*[@id="app"]/div/div[1]/div[2]/input', 10024)

    #定位 搜索 按钮
    def click_sousuo_button(self):
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[1]/div[2]/span')

    #定位到 华药生物 按钮
    def go_to_huayaoshengwu_button(self):
        #return self.base_P.element_wait('xpath->//*[@id="app"]/div/div[3]/ul/li[1]/div/img')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[3]/ul/li[1]/div/img')


    #定位 华药生物  搜索框,并且输入商品ID
    def go_to_huayaoshengwu_sousuokuang(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div/div[2]/div[1]/div[1]/input')
        return self.base_P.clear_type('xpath->//*[@id="app"]/div/div/div[2]/div[1]/div[1]/input', 10532)

    #定位 华药生物  搜索框  搜索按钮
    def go_to_huayaoshengwu_sousuo_button(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[1]/div[2]/span')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[1]/div[2]/span')

    '''
    下面区域是推荐位管理区域
    '''

    #查看 首页 导航栏中  新客推荐栏  是否有商品展示
    def xin_ke_tui_jian_product_zhanshi(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[4]/div/div/div[2]/ul/li[1]/div[1]/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[4]/div/div/div[2]/ul/li[1]/div[1]/span')

    #定位新客推荐更多  按钮，进入新客推荐列表详情页
    def go_to_xinketuijian_page(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[4]/div/div/div[1]/div[4]/span[1]')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[4]/div/div/div[1]/div[4]/span[1]')

    #定位新客推荐列表详情页商品名称
    def check_xinketuijian_product_name(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/div[1]/ul/li[1]/div[2]/div[1]/p[1]/span')
        return self.base_P.get_text(
            'xpath->//*[@id="app"]/div/div[2]/div[1]/ul/li[1]/div[2]/div[1]/p[1]/span')

    #页面滑动到 特价抢购 推荐位，
    def check_tejiaqianggou_page(self):
        # 等待 特价抢购 推荐位出现
        return self.base_P.element_wait('xpath->//*[@id="app"]/div/div[5]/div/div[1]/div[2]/img')

        self.base_P.js_to_element('xpath->//*[@id="app"]/div/div[5]/div/div[1]/div[2]/img')


    # 定位特价抢购 页面的商品名称
    def check_tejiaqianggou_product_name(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[5]/div/div[2]/ul[1]/li[1]/div[1]/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[5]/div/div[2]/ul[1]/li[1]/div[1]/span')

    #定位特价抢购  的  更多 按钮
    def find_tejiaqianggou_gengduo_button(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[5]/div/div[1]/div[4]')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[5]/div/div[1]/div[4]')
    # 定位 特价抢购列表详情页的商品名称是否存在
    def check_tejiaqianggou_liebiao(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/ul/li[2]/p[1]/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/ul/li[2]/p[1]/span')

    #定位特价抢购 商品列表页，商品是否有 会员可见 字样
    def check_tejiaqianggou_product_huiyuankejian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/ul/li[2]/div[1]')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/ul/li[2]/div[1]')

    '''
           通栏图片区域

       '''
    #检查通栏图片是否有跳转链接
    def click_tonglantupian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[6]/div/a/img')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[6]/div/a/img')
    #定位通栏图片的商品列表是否有商品
    def check_tonglantupian_product_list(self):
        #定位商品名称
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/div/div[2]/ul/li[1]/div[2]/div/p[1]/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/div/div[2]/ul/li[1]/div[2]/div/p[1]/span')
    #定位通栏图片的商品列表商品是否有 会员可见  字样
    def check_tonglantupian_product_huiyuankejian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/div/div[2]/ul/li[1]/div[2]/div/p[4]/span/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/div/div[2]/ul/li[1]/div[2]/div/p[4]/span/span')
    '''
    优惠商品推荐位
    '''
    #定位首页优惠商品推荐位 是否有商品名称
    def youhuishangpin_product_name(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[7]/div/div[2]/ul/li[1]/div[1]/div')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[7]/div/div[2]/ul/li[1]/div[1]/div')

    # 定位首页优惠商品推荐位 是否商品有会员可见 字样
    def youhuishangpin_huiyuankejian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[7]/div/div[2]/ul/li[1]/div[2]')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[7]/div/div[2]/ul/li[1]/div[2]')
    #定位优惠商品 更多按钮，进入 优惠商品 列表详情页
    def youhuishangpin_product_list(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[7]/div/div[1]/div[4]')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[7]/div/div[1]/div[4]')

    # 定位优惠商品 列表详情页，是否有商品名称
    def youhuishangpin_product_name(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/ul/li[2]/p[1]/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/ul/li[2]/p[1]/span')
    # 定位优惠商品 列表详情页，商品是否有会员可见 字样
    def youhuishangpin_product_huiyuankejian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/ul/li[2]/div[1]')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/ul/li[2]/div[1]')
    '''
    严选商品
    '''
    #定位首页  严选商品  是否有商品名称
    def yanxuanshangpin_product(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[8]/div/div/div[2]/ul/span/li[2]/div[2]/div[1]')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[8]/div/div/div[2]/ul/span/li[2]/div[2]/div[1]')
    # 定位首页  严选商品  是否有 会员可见字样
    def yanxuanshangpin_huiyuankejian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[8]/div/div/div[2]/ul/span/li[1]/div[2]/div[2]')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[8]/div/div/div[2]/ul/span/li[1]/div[2]/div[2]')
    #定位首页  严选商品  点击更多按钮，进入 严选商品 列表详情页
    def yanxuanshangpin_product_list(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[8]/div/div/div[1]/div[4]/span[1]')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[8]/div/div/div[1]/div[4]/span[1]')
    # 定位，商品详情页是否有商品名称
    def yanxuanshangpin_find_product_name(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/ul/li[1]/div[1]/p[1]/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/ul/li[1]/div[1]/p[1]/span')
    # 定位，商品详情页是否有会员可见
    def yanxuanshangpin_find_huiyuankejian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/ul/li[1]/div[1]/div')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/ul/li[1]/div[1]/div')
    '''
    旗舰店商家
    '''
    #查看旗舰店商家 店铺是否有名称
    def qijiandianshangjia(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[9]/div/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/p')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[9]/div/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/p')
    # 查看旗舰店商家 店铺是否有会员可见
    def qianjianguanshangjia_huiyuankejian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[9]/div/div/div[2]/div/div[1]/ul/li[1]/div[2]')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[9]/div/div/div[2]/div/div[1]/ul/li[1]/div[2]')

    # 旗舰店商家，点击 进店，查看是否有商品展示出来
    def qijianguan_jindian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[9]/div/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/div')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[9]/div/div/div[2]/div/div[1]/div/ul/li[2]/div[1]/div')
    # 定位店铺主页是否有商品名称
    def qijianguan_dianpu_product_lisr(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div/ul/li[1]/div/span[1]/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div/ul/li[1]/div/span[1]/span')
    # 定位店铺主页是否有 会员可见
    def qijianguan_dianpu_huiyuankejian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div/ul/li[1]/div/div/span')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div/ul/li[1]/div/div/span')

    '''
    好货推荐
    '''
    #定位好货推荐商品名称
    def haohuotuijian(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[11]/div/div/div[2]/ul/li[1]/div[1]')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[11]/div/div/div[2]/ul/li[1]/div[1]')
    '''
    点击会员可见，页面跳转到 注册登入页面
    '''
    #点击会员可见，页面跳转到 注册登入页面
    def click_huiyuankejian_to_login(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[4]/div/div/div[2]/ul/li[1]/div[2]')
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[4]/div/div/div[2]/ul/li[1]/div[2]')

    # 定位 跳转页面是否有  验证码登入  字样
    def click_huiyuankejian_to_login_page(self):
        self.base_P.element_wait('xpath->//*[@id="app"]/div/div[2]/div[1]/p[1]')
        return self.base_P.get_text('xpath->//*[@id="app"]/div/div[2]/div[1]/p[1]')



















