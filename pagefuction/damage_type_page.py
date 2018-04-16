'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import damage_type_element
import time
from selenium.webdriver.common.keys import Keys

class DamageTypePage:
    def __init__(self,driver):
        self.driver = driver

    def add_damagetype(self,typename):
        #点击新增按钮
        comfunc.wait(self.driver, damage_type_element.add_type_button)
        self.driver.find_element_by_xpath(damage_type_element.add_type_button).click()
        #输入类型名
        comfunc.wait(self.driver, damage_type_element.add_typename)
        self.driver.find_element_by_xpath(damage_type_element.add_typename).send_keys(typename)
        time.sleep(1)
        #点击确定
        comfunc.wait(self.driver, damage_type_element.add_savebutton)
        self.driver.find_element_by_xpath(damage_type_element.add_savebutton).click()

    def is_element_dispear(self,ele):
        # comfunc.wait_noelement(self.driver,damage_type_element.add_typename)
        comfunc.wait_noelement(self.driver, ele)

    def edit_damagetype(self,typename):
        #点击修改按钮
        comfunc.wait(self.driver, damage_type_element.edit_type_button)
        self.driver.find_element_by_xpath(damage_type_element.edit_type_button).click()
        #输入类型名
        comfunc.wait(self.driver, damage_type_element.add_typename)
        self.driver.find_element_by_xpath(damage_type_element.add_typename).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(damage_type_element.add_typename).send_keys(Keys.DELETE)
        #clear()报错：selenium.common.exceptions.InvalidElementStateException: Message: invalid element state: Element is not currently interactable and may not be manipulated
        #3.19.改成(Keys.CONTROL + "a")
        # self.driver.find_element_by_xpath(damage_type_element.add_typename).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(damage_type_element.add_typename).send_keys(typename)
        time.sleep(1)
        #点击确定
        comfunc.wait(self.driver, damage_type_element.add_savebutton)
        self.driver.find_element_by_xpath(damage_type_element.add_savebutton).click()


    def delete_damagetype(self):
        #点击删除按钮
        comfunc.wait(self.driver, damage_type_element.delete_type_button)
        self.driver.find_element_by_xpath(damage_type_element.delete_type_button).click()
        #点击删除确认按钮
        comfunc.wait(self.driver, damage_type_element.delete_confirm_button)
        self.driver.find_element_by_xpath(damage_type_element.delete_confirm_button).click()

    def click_damage_goods_menu(self):
        comfunc.wait(self.driver,damage_type_element.damage_goods_menu)
        self.driver.find_element_by_xpath(damage_type_element.damage_goods_menu).click()