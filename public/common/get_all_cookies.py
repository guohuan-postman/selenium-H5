from selenium import webdriver
from time import sleep
class Get_All_cookie():
    def get_cookie(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://release.yaodouwang.com/login?redirect=%2Fshopping_cart')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/p[2]').click() #点击密码登录按钮
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/input[1]').send_keys(18911111111) #点击请输入手机号输入框
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/input[2]').send_keys(123456) #点击请输入密码
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/input[3]').click() #点击登录按钮
        '''
        iframe = driver.find_element_by_xpath("//iframe[@id='iframe-login']")
        #定位嵌套页面
        driver.switch_to_frame(iframe)
        #进入该嵌套页面
        driver.find_element_by_css_selector("[name='mail']").send_keys('邮箱')
        driver.find_element_by_css_selector("[name='pass']").send_keys('密码')
        driver.find_element_by_css_selector('.button-teal').click()
        '''
        #登录
        cookie = driver.get_cookies()
        print(cookie)
        #driver.delete_all_cookies()
        sleep(1)
        driver.refresh()
        return cookie