import unittest
from public.common import pyselenium
from config import globalparam
from public.common.log import Log
from public.handle.login_handle import Login_Handle
from selenium import webdriver
import time
from public.pages.base_page import Base_Page



def aa():

    WIDTH = 375
    HEIGHT = 812
    PIXEL_RATIO = 3.0
    UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

    mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                       "userAgent": UA}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
    selenium_driver = webdriver.Chrome(options=chrome_options)  # 移动端配置
    selenium_driver.maximize_window()
    selenium_driver.accept_next_alert = True
    # self.selenium_driver = webdriver.Chrome()
    selenium_driver.get('http://192.168.0.120:30180')
    time.sleep(3)
    weizhi2 = selenium_driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[5]/div/div[1]/div[2]/img')  # 先定位到一个元素
    selenium_driver.execute_script("arguments[0].scrollIntoView();", weizhi2)  # 让其滚动到这个坐标
    time.sleep(5)



def bb():
    time.sleep(3)





if __name__ == '__main__':
    aa()

    bb()
