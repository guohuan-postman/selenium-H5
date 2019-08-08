import time
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions

"""设置手机的大小"""
WIDTH = 375
HEIGHT = 812
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                   "userAgent": UA}

options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://192.168.0.120:30180')
driver.maximize_window()
"""定位操作元素"""
button = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/ul/li[2]/div/img')
time.sleep(3)
Action = TouchActions(driver)
"""从button元素像下滑动200元素，以50的速度向下滑动"""
Action.flick_element(button, 0, -200, 50).perform()
time.sleep(5)
driver.close()

''''''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('file:///C:/Users/hunk/Desktop/demo_clicks.html')
driver.maximize_window()
# 首先我们需要获取到要操作的元素，然后再次进行操作
doubleButtonElement = driver.find_element_by_xpath('/html/body/form/input[2]')   #获取双击按钮元素
buttonElement = driver.find_element_by_xpath('/html/body/form/input[3]')         #获取单击按钮元素
rightButtonElement = driver.find_element_by_xpath('/html/body/form/input[4]')    #获取右击按钮元素
clickHoldElement = driver.find_element_by_xpath('/html/body/form/input[5]')      #获取按住不放按钮元素
'''内容开始的时候我们也介绍说明，当调用perform()方法时才会执行鼠标操作'''
#双击操作
ActionDoubleClick= ActionChains(driver).double_click(doubleButtonElement)
ActionDoubleClick.perform()
time.sleep(3)
# 单击操作
ActionClick = ActionChains(driver).click(buttonElement)
ActionClick.perform()
time.sleep(3)
# 右击操作
ActionContextClick = ActionChains(driver).context_click(rightButtonElement)
ActionContextClick.perform()
time.sleep(3)
#按住不放左键
ActionClickHold = ActionChains(driver).click_and_hold(clickHoldElement)
ActionClickHold.perform()
time.sleep(3)
driver.quit()