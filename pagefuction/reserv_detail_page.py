'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import reserv_detail_element
import time
from selenium.webdriver.common.action_chains import ActionChains

class ReservDetailPage:
    def __init__(self,driver):
        self.driver = driver

    #cancel_reserv_button元素找不到
    def cancel_reserv(self):
        comfunc.wait(self.driver,reserv_detail_element.more_operation_button)
        # chain = ActionChains(self.driver)
        # chain.move_to_element(reserv_detail_element.more_operation_button)
        # chain.perform()
        obj = self.driver.find_element_by_xpath(reserv_detail_element.more_operation_button)
        ac = ActionChains(self.driver).move_to_element(obj).perform()
        # comfunc.wait(self.driver, reserv_detail_element.cancel_reserv_button)
        time.sleep(1)
        self.driver.find_element_by_xpath(reserv_detail_element.cancel_reserv_button).click()

    
