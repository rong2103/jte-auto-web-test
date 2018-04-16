'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import damage_goods_element
import time
from selenium.webdriver.common.keys import Keys

class DamageGoodsPage:
    def __init__(self,driver):
        self.driver = driver

    def add_damagegoods(self,goodsname,comprice,price,beizhu):
        #点击新增按钮
        comfunc.wait(self.driver, damage_goods_element.add_goods_button)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_button).click()
        #选择物品类型
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_type_select).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_type_value).click()
        #输入物品名
        comfunc.wait(self.driver, damage_goods_element.add_goodsname)
        self.driver.find_element_by_xpath(damage_goods_element.add_goodsname).send_keys(goodsname)
        time.sleep(1)
        #输入赔偿单价
        comfunc.wait(self.driver, damage_goods_element.add_goods_compPrice)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_compPrice).send_keys(comprice)
        #输入成本价
        comfunc.wait(self.driver, damage_goods_element.add_goods_price)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_price).send_keys(price)
        #输入备注
        comfunc.wait(self.driver, damage_goods_element.add_goods_beizhu)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_beizhu).send_keys(beizhu)
        time.sleep(2)
        #点击保存
        # comfunc.wait(self.driver, damage_goods_element.add_goodsname)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_savebutton).click()

    def edit_damagegoods(self,goodsname,comprice,price,beizhu):
        #点击修改按钮
        comfunc.wait(self.driver, damage_goods_element.edit_goods_button)
        self.driver.find_element_by_xpath(damage_goods_element.edit_goods_button).click()
        # #选择物品类型
        # self.driver.find_element_by_xpath(damage_goods_element.add_goods_type_select).click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath(damage_goods_element.add_goods_type_value).click()
        #输入物品名
        comfunc.wait(self.driver, damage_goods_element.add_goodsname)
        self.driver.find_element_by_xpath(damage_goods_element.add_goodsname).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(damage_goods_element.add_goodsname).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(damage_goods_element.add_goodsname).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(damage_goods_element.add_goodsname).send_keys(goodsname)
        time.sleep(1)
        #输入赔偿单价
        comfunc.wait(self.driver, damage_goods_element.add_goods_compPrice)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_compPrice).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_compPrice).send_keys(comprice)
        #输入成本价
        comfunc.wait(self.driver, damage_goods_element.add_goods_price)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_price).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_price).send_keys(price)
        #输入备注
        comfunc.wait(self.driver, damage_goods_element.add_goods_beizhu)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_beizhu).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_beizhu).send_keys(beizhu)
        time.sleep(2)
        #点击保存
        # comfunc.wait(self.driver, damage_goods_element.add_goodsname)
        self.driver.find_element_by_xpath(damage_goods_element.add_goods_savebutton).click()

    def delete_damagegoods(self):
        #点击删除按钮
        comfunc.wait(self.driver, damage_goods_element.delete_goods_button)
        self.driver.find_element_by_xpath(damage_goods_element.delete_goods_button).click()
        #点击删除确认按钮
        comfunc.wait(self.driver, damage_goods_element.delete_confirm_button)
        self.driver.find_element_by_xpath(damage_goods_element.delete_confirm_button).click()

    def is_element_disappear(self,ele):
        comfunc.wait_noelement(self.driver,ele)
