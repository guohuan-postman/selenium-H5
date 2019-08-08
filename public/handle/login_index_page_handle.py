from public.pages.login_index_page import Login_Index_Page
from public.pages.base_page import Base_Page
import time



class Login_Index_Page_Handle(object):

    def __init__(self,selenium_driver):
        self.Login_i_p = Login_Index_Page(selenium_driver)

    '''
    def click_to_login_page(self):
        self.Login_i_p.click_button_to_login_button_page()
    '''

    def login(self,phone_n,password_num):
        self.Login_i_p.click_button_to_login_button_page().click()
        self.Login_i_p.input_phone_number(phone_n)
        self.Login_i_p.input_password(password_num)
        self.Login_i_p.click_login_button().click()


    def not_found_input_kuang(self):
        self.Login_i_p.check_login_button_not_exit()



