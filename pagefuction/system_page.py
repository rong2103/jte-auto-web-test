'''
系统页面操作方法
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-

from common import comfunc
from pageelement import system_element

class SystemPage:

    def __init__(self,driver):
        self.driver = driver

    #点击基础设施按钮
    def click_infrastructure(self):
        comfunc.wait(self.driver,system_element.infrastructure_button_locator)
        self.driver.find_element_by_xpath(system_element.infrastructure_button_locator).click()

    #点击损物赔偿按钮
    def click_damagegoods(self):
        comfunc.wait(self.driver,system_element.loss_button_locator)
        self.driver.find_element_by_xpath(system_element.loss_button_locator).click()

    #点击租赁物品按钮
    def click_hiregoods(self):
        comfunc.wait(self.driver,system_element.hire_button_locator)
        self.driver.find_element_by_xpath(system_element.hire_button_locator).click()