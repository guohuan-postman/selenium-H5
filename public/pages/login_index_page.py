from public.pages.base_page import Base_Page

class Login_Index_Page(object):

    def __init__(self,selenium_driver):
        self.base_P = Base_Page(selenium_driver)

    def click_button_to_login_button_page(self):
        #点击登入按钮
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[2]/div[1]/p[2]')

    def input_phone_number(self,phone_n):

        # 输入用户名
        return self.base_P.type('xpath->//*[@id="app"]/div/div[2]/form[2]/input[1]',phone_n)
        #return self.base_P.get_element('xpath->//*[@id="app"]/div/div[2]/form[2]/input[1]').send_keys(phone_n)

    def input_password(self,password_num):
        #输入密码
        #return self.base_P.get_element('xpath->//*[@id="app"]/div/div[2]/form[2]/input[2]').send_keys(password_num)
        return self.base_P.type('xpath->//*[@id="app"]/div/div[2]/form[2]/input[2]',password_num)

    def click_login_button(self):
        #点击登入按钮
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[2]/form[2]/input[3]')

    def check_login_button_not_exit(self):
        #找不到  忘记密码 ?
        #a_href = get_12306.find_element_by_xpath('//*[@id="app"]/div/div[2]/form[2]/p/a')
        ele = self.base_P.get_element('xpath->//*[@id="app"]/div/div[2]/form[2]/p/a')
        return ele.get_attribute('textContent')
        #return ss.text
        #ss = self.base_P.get_element('xpath->//*[@id="app"]/div/div[2]/div[2]/span')
        #return ss.get_attribute('textContent')
        #return self.base_P.get_attribute('xpath->//*[@id="app"]/div/div[2]/div[2]/span', 'textContent')





