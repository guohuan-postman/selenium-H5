from public.common.basepage import Page

class Search_product(Page):



    def click_search_text(self):
        #点击搜索框
        self.dr.click('xpath->//*[@id="app"]/div/div[1]/div[1]/p')


    def input_product_number(self):
        #输入搜索产品编号
        self.dr.type('xpath->//*[@id="app"]/div/div[1]/div[2]/input',99093)

    def click_sousuo_button(self):
        #点击搜索按钮
        self.dr.click('xpath->//*[@id="app"]/div/div[1]/div[2]/span')

    def product_name_test(self):
        #获取搜索出来的产品名称
        return self.dr.get_text('xpath->//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div/p[1]/span')

