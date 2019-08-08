import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from public.common.log import Log
from selenium import webdriver
from public.handle.weidengru_index_page_handle import Weidengru_index_page_handle
import time
class weidengru_index_page_test(unittest.TestCase):

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
        self.selenium_driver.get('http://192.168.0.120:30180')
        self.selenium_driver.accept_next_alert = True
        self.weidengru_handle = Weidengru_index_page_handle(self.selenium_driver)


    def tearDown(self):

        self.logger = Log()
        self.selenium_driver.quit()
        self.logger.info('###############################  End  ###############################')


    #首页 搜索框 搜索商品
    def test_dingwei_product_name_not_null(self):
        self.weidengru_handle.shouye_sousuokuang_handle()
        time.sleep(1)
        #定位商品名称
        product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/p[1]/span').text
        # 断言搜索商品名称不为空
        self.assertIsNotNone(product_name,msg='如果此条失败，证明没有搜索出来查询的商品信息，没有定位到商品名称，需要查看首页搜索是否可用')
        self.assertEqual(product_name, '吉非罗齐胶囊', msg='商品名称不一致')

    
    #化药生物分类页面，查看是否分类有数据可用
    def test_huayaoshengwu_fenlei_page_product_name_not_null(self):
        time.sleep(3)
        #点击华药生物 按钮进入 分类详情页
        self.weidengru_handle.go_to_huayaoshengwu_button_handle()
        time.sleep(3)
        # 定位华药生物 分类 商品名称
        WebDriverWait(self.selenium_driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]')))
        huayao_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/p[1]').text
        time.sleep(3)
        #断言 华药生物 页面商品名称 数据不为空，分类页面有商品信息
        self.assertIsNotNone(huayao_product_name, msg='如果此条失败，证明化药生物分类详情页面无数据，需要查看是否华药生物 分类 页面可用')
        self.assertEqual('吲达帕胺(寿比山片)', huayao_product_name,msg='失败就没找到，吲达帕胺(寿比山片)')



    def test_huayaoshengwu_fenlei_page_product_name_not_null(self):
        time.sleep(3)
        # 点击华药生物 按钮进入 分类详情页
        self.weidengru_handle.go_to_huayaoshengwu_button_handle()
        time.sleep(1)
        # 定位华药生物 分类 商品名称
        WebDriverWait(self.selenium_driver, 10, 1).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/p[1]/span')))
        huayao_product_name = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/p[1]/span').text
        time.sleep(1)

        # 断言 在 未登入 的时候，有 会员可见 字样
        #self.assertEqual('会员可见', msg='如果断言失败，证明没有找到会员可见字样，这不是未登入状态或者页面无商品数据')
        self.assertEqual(huayao_product_name,'会员可见', msg='如果断言失败，证明没有找到会员可见字样，这不是未登入状态或者页面无商品数据')


 
    # 化药生物分类页面，查看是否可以搜索商品
    def test_huayaoshengwu_fenlei_page_huiyuankejian(self):
        time.sleep(3)
        # 点击华药生物 按钮进入 分类详情页
        self.weidengru_handle.go_to_huayaoshengwu_button_handle()
        time.sleep(3)
        #点击分类搜索框，输入商品ID，并点击搜索按钮
        self.weidengru_handle.sousuo_huayaoshengwu_product()
        time.sleep(3)
        #定位搜索搜索出来了的商品名称,
        WebDriverWait(self.selenium_driver, 10, 1).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div/p[1]/span')))
        sousuo_huayaoshengwu_product_name = self.selenium_driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div/p[1]/span').text
        #断言搜索出来的商品名称不是空的
        #self.assertIsNotNone(sousuo_huayaoshengwu_product_name, msg='如果用例失败，证明没有搜索出来相关的商品，请查看华药生物分类里的搜索功能是否可用')
        self.assertEqual(sousuo_huayaoshengwu_product_name,'马来酸依那普利片', msg='马来酸依那普利片，这个药品名称没有搜索找到。请查看华药生物分类里的搜索功能是否可用')


        # 化药生物分类页面，查看搜索出来的商品，是否有会员可见字样
    def test_huayaoshengwu_fenlei_page(self):
        time.sleep(3)
        # 点击华药生物 按钮进入 分类详情页
        self.weidengru_handle.go_to_huayaoshengwu_button_handle()
        time.sleep(3)
        # 点击分类搜索框，输入商品ID，并点击搜索按钮
        self.weidengru_handle.sousuo_huayaoshengwu_product()
        time.sleep(3)
        # 定位搜索搜索出来了的商品名称,
        WebDriverWait(self.selenium_driver, 10, 1).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/p[1]/span')))
        sousuo_huayaoshengwu_huiyuankejian = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/p[1]/span').text

        # 断言搜索出来的商品名称不是空的
        #self.assertIsNotNone(sousuo_huayaoshengwu_huiyuankejian, msg='如果用例失败，证明没有搜索出来相关的商品，请查看华药生物分类里的搜索功能是否可用')
        self.assertEqual('会员可见',sousuo_huayaoshengwu_huiyuankejian,msg='会员可见字体找不到，请查看华药生物分类里的搜索功能是否可用')

        

    #新客推荐栏中，商品信息展示的名称是不是 一个套餐把
    def test_xin_ke_tui_jian_product_zhanshi(self):
        yigetaocanba = self.weidengru_handle.xin_ke_tui_jian_product_zhanshi_handle()
        self.assertEqual('一个套餐把', yigetaocanba, msg='没有返回商品名称，一个套餐把，证明没有找到这个商品或者，首页没有新客推荐 推荐位')

    # 点击新客推荐更多  按钮，进入新客推荐列表详情页
    def test_go_to_xinketuijian_page(self):
        self.weidengru_handle.go_to_xinketuijian_page_handle()
        first_product_name = self.weidengru_handle.check_xinketuijian_product_name_handle()
        self.assertEqual('一个套餐把',first_product_name,msg='如果断言失败，证明没有找到 一个套餐把 商品名称，或者列表没有展示出来商品。请检查新客推荐->更多,是否可用')
   
    
    # 检查特价抢购 页面的商品名称
    def test_check_tejiaqianggou_page(self):
        time.sleep(3)
        # 页面滑动到 特价抢购 推荐位
        self.weidengru_handle.check_tejiaqianggou_page_handle()
        tejiaqianggou_product_name = self.weidengru_handle.check_tejiaqianggou_product_name_handle()
        time.sleep(3)
        self.assertEqual('让你看看对不对！', tejiaqianggou_product_name,msg='没有找到特价抢购 推荐位，的商品。请查看是否滑动到了此列，或者是否展示出来了，让你看看对不对！，这个商品 ')
    
    #检查特价抢购  的  更多 按钮，特价抢购 详情页是否有商品
    def test_find_tejiaqianggou_gengduo_button(self):
        time.sleep(2)
        # 页面滑动到 特价抢购 推荐位
        #定位到 新客推荐，可以查看到 特价抢购栏
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[4]/div/div/div[1]/div[2]/img')  # 先定位到一个元素  定位到 新客推荐，
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        #点击特价抢购  的  更多 按钮，进入 特价抢购商品列表详情页
        self.weidengru_handle.find_tejiaqianggou_gengduo_button_handle()
        #获取 特价抢购列表详情页的商品名称是否存在
        duoyuanweisupian = self.weidengru_handle.check_tejiaqianggou_liebiao_handle()
        self.assertEqual(duoyuanweisupian, '多维元素片(21金维他)', msg='如果断言失败，证明没有找到商品名称，请检查特价抢购列表页面，是否有商品展示出来')
        tejiaqianggou_product_name_huiyuankejian = self.weidengru_handle.check_tejiaqianggou_product_huiyuankejian_handle()
        self.assertEqual(tejiaqianggou_product_name_huiyuankejian,'会员可见',msg='如果用例失败，证明没有找到会员可见字样，请检查特价抢购列表详情页，商品在未登入情况下，是否显示会员可见图标')
    
    def test_click_tonglantupian(self):
        time.sleep(2)
        # 页面滑动到 特价抢购 推荐位
        # 定位到 新客推荐，可以查看到 特价抢购栏
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[5]/div/div[1]/div[4]/span[1]')  # 先定位到一个元素  定位到 特价抢购 的更多，
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        #点击通栏图片进入活动专题页面
        self.weidengru_handle.click_tonglantupian_handle()
        time.sleep(2)
        #获取商品名称
        tonglantupian_product_name = self.weidengru_handle.check_tonglantupian_product_list_handle()
        self.assertEqual('234567',tonglantupian_product_name, msg='如果断言失败，证明没有找到商品，请检查通栏图片的商品列表中，是否有商品，并且可以跳转成功')
   
    #检查通栏图片的商品列表商品是否有 会员可见  字样
    def test_check_tonglantupian_product_huiyuankejian(self):
        time.sleep(2)
        # 页面滑动到 特价抢购 推荐位
        # 定位到 新客推荐，可以查看到 特价抢购栏
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[5]/div/div[1]/div[4]/span[1]')  # 先定位到一个元素  定位到 特价抢购 的更多，
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        # 点击通栏图片进入活动专题页面
        self.weidengru_handle.click_tonglantupian_handle()
        time.sleep(2)
        
    

    # 断言首页优惠商品推荐位 是否有商品名称
    def test_youhuishangpin_product_name(self):
        time.sleep(2)
        # 页面滑动到 优惠商品 推荐位
        # 定位到 通栏图片，可以查看到 优惠商品 推荐位
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div/a/img')  # 先定位到一个元素  定位到 通栏图片区域
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        # 查看首页优惠商品推荐位 是否有商品名称
        youhuishangpin_product_name_ = self.weidengru_handle.youhuishangpin_product_name_handle()
        self.assertEqual(youhuishangpin_product_name_,'让你看看对不对！', msg='如果用例失败，证明没有找到商品名称。请查看优惠商品 推荐位是否有商品展示出来')
    

    # 断言首页优惠商品推荐位 是否商品有会员可见字样
    def test_youhuishangpin_huiyuankejian(self):
        time.sleep(2)
        # 页面滑动到 优惠商品 推荐位
        # 定位到 通栏图片，可以查看到 优惠商品 推荐位
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div/a/img')  # 先定位到一个元素  定位到 通栏图片区域
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        # 查看首页优惠商品推荐位 是否有商品名称
        youhuishangpin_product_name_ = self.weidengru_handle.youhuishangpin_huiyuankejian_handle()
        self.assertEqual(youhuishangpin_product_name_,'会员可见', msg='如果用例失败，证明没有找到会员可见。请查看优惠商品 推荐位是否有商品展示出来 会员可见 字样')
        
    

    # 点击优惠商品 更多按钮，进入 优惠商品 列表详情页
    def test_youhuishangpin_product_list(self):
        time.sleep(2)
        # 页面滑动到 优惠商品 推荐位
        # 定位到 通栏图片，可以查看到 优惠商品 推荐位
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div/a/img')  # 先定位到一个元素  定位到 通栏图片区域
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        #点击优惠商品 更多按钮
        self.weidengru_handle.youhuishangpin_product_list_handle()
        #断言优惠商品 列表详情页，是否有商品名称
        youhuishangpin_product_name = self.weidengru_handle.youhuishangpin_product_name_handle()
        self.assertEqual(youhuishangpin_product_name, '复方半边莲注射液',msg='如果用例失败，证明没有找到商品名称。请查看 优惠商品->更多 是否有商品展示出来')
    
    # 点击优惠商品 更多按钮，进入 优惠商品 列表详情页
    def test_youhuishangpin_product_list(self):
        time.sleep(2)
        # 页面滑动到 优惠商品 推荐位
        # 定位到 通栏图片，可以查看到 优惠商品 推荐位
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div/a/img')  # 先定位到一个元素  定位到 通栏图片区域
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        # 点击优惠商品 更多按钮
        self.weidengru_handle.youhuishangpin_product_list_handle()

        # 断言优惠商品 列表详情页，会员可见字样
        youhuishangpin_huiyuankejian = self.weidengru_handle.youhuishangpin_product_huiyuankejian_handle()
        self.assertEqual(youhuishangpin_huiyuankejian, '会员可见', msg='如果用例失败，证明没有找到商品名称。请查看 优惠商品->更多 是否有  会员可见  字样 展示出来')
        
    

    # 定位首页  严选商品  是否有商品名称
    def test_yanxuanshangpin_product(self):
        time.sleep(2)
        # 页面滑动到 严选商品 推荐位
        # 定位到 优惠商品，可以查看到 严选商品 推荐位
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div/div[1]/div[2]/img')  # 先定位到一个元素  定位到 优惠商品区域
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        #断言首页  严选商品  是否有商品名称
        yanxuanshangpin_product_name = self.weidengru_handle.yanxuanshangpin_product_handle()
        self.assertEqual(yanxuanshangpin_product_name,'维生素AD滴剂(2000:700)（鑫烨）',msg='如果用例失败，证明没有找到商品名称，请检查，严选商品推荐位的商品列表是否有商品展示出来')

        # 断言首页  严选商品  是否有 会员可见字样
        yanxuanshangpin_huiyuankejian = self.weidengru_handle.yanxuanshangpin_huiyuankejian_handle()
        self.assertEqual(yanxuanshangpin_huiyuankejian,'会员可见',msg='如果用例失败，证明没有找到  会员可见，请检查，严选商品推荐位的商品列表是否有会员可见字样展示出来')
        
      
    # 定位首页  严选商品  点击更多 进入 严选商品商品列表详情页
    def test_yanxuanshangpin_product_list(self):
        time.sleep(2)
        # 页面滑动到 严选商品 推荐位
        # 定位到 优惠商品，可以查看到 严选商品 推荐位
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div/div[1]/div[2]/img')  # 先定位到一个元素  定位到 优惠商品区域
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        # 定位首页  严选商品  点击更多
        self.weidengru_handle.yanxuanshangpin_product_list_handle()
        time.sleep(2)
        #检查，商品详情页是否有商品名称
        yanxuanxiangqing_product_name = self.weidengru_handle.yanxuanshangpin_find_product_name_handle()
        self.assertEqual(yanxuanxiangqing_product_name,'让你看看对不对！',msg='如果用例失败，证明没有找到商品名称，请检查，严选商品->更多，列表详情页是否有商品展示出来')
        # 检查，商品详情页是否有会员可见
        yanxuanshangpin_huiyuankejian = self.weidengru_handle.yanxuanshangpin_find_huiyuankejian_handle()
        self.assertEqual(yanxuanshangpin_huiyuankejian,'会员可见',msg='如果用例失败，证明没有找到会员可见，请检查，严选商品->更多，列表详情页是否有会员可见展示出来')
        
    #旗舰店商家，是否有店铺
    def test_qijiandianshangjia(self):
        time.sleep(2)
        # 页面滑动到 旗舰店商家 推荐位
        # 定位到 严选商品，可以查看到 旗舰店商家 推荐位
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[8]/div/div/div[1]/div[2]/img')  # 先定位到一个元素  定位到 严选商品 区域
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        #查看是否展示出来了店铺
        qijiandian_dianpu_name = self.weidengru_handle.qijiandianshangjia_handle()
        self.assertEqual(qijiandian_dianpu_name,'名博药业',msg='如果用例失败，证明 没有找到店铺名称，请检查旗舰馆商家是否有 店铺 展示出来')
        #检查是否有 会员可见 字样
        qijianguan_huiyuankejian = self.weidengru_handle.qianjianguanshangjia_huiyuankejian_handle()
        self.assertEqual(qijianguan_huiyuankejian,'会员可见',msg='如果用例失败，证明 没有找到会员可见，请检查旗舰馆商家是否有 会员可见 展示出来')
     
    # 断言旗舰店商家，点击 进店，查看是否有商品展示出来
    def test_qijiandianshangjia(self):
        time.sleep(2)
        # 页面滑动到 旗舰店商家 推荐位
        # 定位到 严选商品，可以查看到 旗舰店商家 推荐位
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[8]/div/div/div[1]/div[2]/img')  # 先定位到一个元素  定位到 严选商品 区域
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        #点击 进店 按钮 进入店铺主页
        self.weidengru_handle.qijianguan_jindian_handle()
        #检查店铺主页是否有商品名称
        dianpuzhuye_product_name = self.weidengru_handle.qijianguan_dianpu_product_lisr_handle()
        self.assertEqual(dianpuzhuye_product_name,'健胃消食片0.5g*36片/盒',msg='如果用例失败，证明没有找到商品名称，请检查，旗舰店商家 ->进店 ，是否店铺主页有商品列表')
        # 检查店铺主页是否有 会员可见
        dianpuzhuye_product_huiyuankejian = self.weidengru_handle.qijianguan_dianpu_huiyuankejian_handle()
        self.assertEqual(dianpuzhuye_product_huiyuankejian,'会员可见',msg='如果用例失败，证明没有找到 会员可见，请检查，旗舰店商家 ->进店 ，是否店铺主页有  会员可见')

    # 好货推荐
    def test_haohuotuijian(self):
        time.sleep(2)
        # 页面滑动到 好货推荐 推荐位
        # 定位到 好货推荐，可以查看到 好货推荐 推荐位
        tejiaqianggou_tuijianwei = self.selenium_driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[11]/div/div/div[1]/div[2]/img')  # 先定位到一个元素  定位到 好货推荐 区域
        self.selenium_driver.execute_script("arguments[0].scrollIntoView();", tejiaqianggou_tuijianwei)  # 让其滚动到这个坐标
        time.sleep(2)
        #定位好货推荐商品名称
        haohuotuijian_product_name = self.weidengru_handle.haohuotuijian_handle()
        self.assertEqual(haohuotuijian_product_name, '银翘解毒合剂', msg='如果用例失败，证明没有找到 好货推荐 商品名称，请检查，好货推荐是否有商品展示出来')
        time.sleep(3)

    #点击首页  会员可见，页面跳转到 注册登入页面
    def test_click_huiyuankejian_to_login(self):
        #页面跳转到 注册登入页面
        self.weidengru_handle.click_huiyuankejian_to_login_handle()
        #检查跳转页面是否有  验证码登入  字样

        huiyuankejian_to_login = self.weidengru_handle.click_huiyuankejian_to_login_page_handle()
        time.sleep(3)
        self.assertEqual(huiyuankejian_to_login,'验证码登录',msg='如果用例失败，证明没有跳转到  注册登入页面，请检查  会员可见 页面跳转是否正常 ')

    
    










        


























































