from public.pages.base_page import Base_Page

class Login_Page(object):

    def __init__(self,selenium_driver):

        self.base_P = Base_Page(selenium_driver)

    def click_buy_button_to_login(self):
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[8]/ul/li[2]/a/img[1]')


    def not_found_buycar(self):
        return self.base_P.get_element('xpath->//*[@id="app"]/div/div[8]/ul/li[2]/a/span')
