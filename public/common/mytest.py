#coding=utf-8

import unittest
from public.common import pyselenium
from config import globalparam
from public.common.log import Log


class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    driver = pyselenium.PySelenium(globalparam.browser)
    def setUp(self, dr =driver):
        self.dr = dr
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        #self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.max_window()
        self.dr.accept_next_alert = True

    def tearDown(self):
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')

