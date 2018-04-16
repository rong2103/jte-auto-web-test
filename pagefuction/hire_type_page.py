'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import hire_type_element
import time
from selenium.webdriver.common.keys import Keys

class HireTypePage:
    def __init__(self,driver):
        self.driver = driver

    def add_hiretype(self,typename):
        #点击新增按钮
        comfunc.wait(self.driver,hire_type_element.add_type_button)
        self.driver.find_element_by_xpath(hire_type_element.add_type_button).click()
        #输入类型名称
        comfunc.wait(self.driver, hire_type_element.add_type_name)
        self.driver.find_element_by_xpath(hire_type_element.add_type_name).send_keys(typename)
        time.sleep(1)
        #点击保存按钮
        self.driver.find_element_by_xpath(hire_type_element.add_savebutton).click()

    def edit_hiretype(self,typename):
        #点击修改按钮
        comfunc.wait(self.driver,hire_type_element.edit_type_button)
        self.driver.find_element_by_xpath(hire_type_element.edit_type_button).click()
        #输入类型名称
        comfunc.wait(self.driver, hire_type_element.add_type_name)
        time.sleep(1)
        # self.driver.find_element_by_xpath(hire_type_element.add_type_name).clear()
        self.driver.find_element_by_xpath(hire_type_element.add_type_name).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(hire_type_element.add_type_name).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(hire_type_element.add_type_name).send_keys(typename)
        time.sleep(1)
        #点击保存按钮
        self.driver.find_element_by_xpath(hire_type_element.add_savebutton).click()

    def delete_hiretype(self):
        #点击删除按钮
        comfunc.wait(self.driver,hire_type_element.delete_type_button)
        self.driver.find_element_by_xpath(hire_type_element.delete_type_button).click()
        comfunc.wait(self.driver, hire_type_element.delete_confirm_button)
        self.driver.find_element_by_xpath(hire_type_element.delete_confirm_button).click()


    def is_element_dispear(self,ele):
        comfunc.wait_noelement(self.driver, ele)

    def click_hiregoods_menu(self):
        comfunc.wait(self.driver, hire_type_element.hire_goods_menu)
        self.driver.find_element_by_xpath(hire_type_element.hire_goods_menu).click()



