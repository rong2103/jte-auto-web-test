'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import hire_goods_element
import time
from selenium.webdriver.common.keys import Keys

class HireGoodsPage:
    def __init__(self,driver):
        self.driver = driver

    def add_hiregoods(self, goodsname, price, beizhu):
        #点击新增按钮
        comfunc.wait(self.driver, hire_goods_element.add_goods_button)
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_button).click()
        #选择物品类型
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_select).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_value).click()
        #输入物品名
        comfunc.wait(self.driver, hire_goods_element.add_goodsname)
        self.driver.find_element_by_xpath(hire_goods_element.add_goodsname).send_keys(goodsname)
        time.sleep(1)
        #输入租借单价
        comfunc.wait(self.driver, hire_goods_element.add_goods_compPrice)
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_compPrice).send_keys(price)
        #输入备注
        comfunc.wait(self.driver, hire_goods_element.add_goods_beizhu)
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_beizhu).send_keys(beizhu)
        time.sleep(2)
        #点击保存
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_savebutton).click()

    def edit_hiregoods(self, goodsname, price, beizhu):
        #点击修改按钮
        comfunc.wait(self.driver, hire_goods_element.edit_hiregoods_button)
        self.driver.find_element_by_xpath(hire_goods_element.edit_hiregoods_button).click()
        # #选择物品类型
        # self.driver.find_element_by_xpath(hire_goods_element.add_goods_select).click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath(hire_goods_element.add_goods_value).click()
        #输入物品名
        comfunc.wait(self.driver, hire_goods_element.add_goodsname)
        self.driver.find_element_by_xpath(hire_goods_element.add_goodsname).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(hire_goods_element.add_goodsname).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(hire_goods_element.add_goodsname).clear()
        time.sleep(1)
        self.driver.find_element_by_xpath(hire_goods_element.add_goodsname).send_keys(goodsname)
        #输入租借单价
        comfunc.wait(self.driver, hire_goods_element.add_goods_compPrice)
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_compPrice).clear()
        time.sleep(1)
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_compPrice).send_keys(price)
        #输入备注
        comfunc.wait(self.driver, hire_goods_element.add_goods_beizhu)
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_beizhu).clear()
        time.sleep(1)
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_beizhu).send_keys(beizhu)
        time.sleep(2)
        #点击保存
        self.driver.find_element_by_xpath(hire_goods_element.add_goods_savebutton).click()

    def delete_hiregoods(self):
        #点击删除按钮
        comfunc.wait(self.driver, hire_goods_element.delete_hiregoods_button)
        self.driver.find_element_by_xpath(hire_goods_element.delete_hiregoods_button).click()
        comfunc.wait(self.driver, hire_goods_element.delete_confirm_button)
        self.driver.find_element_by_xpath(hire_goods_element.delete_confirm_button).click()


    def is_element_exist(self,ele):
        comfunc.wait(self.driver,ele)

    def is_element_disappear(self, ele):
        comfunc.wait_noelement(self.driver,ele)
