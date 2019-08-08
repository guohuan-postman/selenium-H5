from public.pages.login_page import Login_Page
from public.common import pyselenium
from config import globalparam

class Login_Handle(object):

    def __init__(self,selenium_driver):

        self.login = Login_Page(selenium_driver)

    def click_to_login_page(self):
        self.login.click_buy_button_to_login().click()

    def find_buycar(self):
        self.login.not_found_buycar()