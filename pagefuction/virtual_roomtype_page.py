'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import virtualroomtype_element
import time
from selenium.webdriver.common.keys import Keys

class VirtualRoomTypePage:
    def __init__(self,driver):
        self.driver = driver

    def add_virtual_roomtype(self,typename,beizhu):
        #点击新增按钮
        comfunc.wait(self.driver, virtualroomtype_element.add_roomtype_button)
        self.driver.find_element_by_xpath(virtualroomtype_element.add_roomtype_button).click()
        #输入界面字段
        #房型
        comfunc.wait(self.driver, virtualroomtype_element.virtual_roomtype_name)
        self.driver.find_element_by_xpath(virtualroomtype_element.virtual_roomtype_name).send_keys(typename)
        #选中实体房型
        self.driver.find_element_by_xpath(virtualroomtype_element.room_type_select).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(virtualroomtype_element.room_type_value).click()
        #描述
        comfunc.wait(self.driver, virtualroomtype_element.beizhu)
        self.driver.find_element_by_xpath(virtualroomtype_element.beizhu).send_keys(beizhu)
        time.sleep(3)
        #点击保存
        self.driver.find_element_by_xpath(virtualroomtype_element.savebutton).click()

    def assert_add(self,ele):
        comfunc.wait_noelement(self.driver,ele)

    def edit_virtual_roomtype(self,typename,beizhu):
        #点击修改按钮
        comfunc.wait(self.driver, virtualroomtype_element.edit_virtual_roomtype_button)
        self.driver.find_element_by_xpath(virtualroomtype_element.edit_virtual_roomtype_button).click()
        #输入界面字段
        #房型
        comfunc.wait(self.driver, virtualroomtype_element.virtual_roomtype_name)
        self.driver.find_element_by_xpath(virtualroomtype_element.virtual_roomtype_name).click()
        self.driver.find_element_by_xpath(virtualroomtype_element.virtual_roomtype_name).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(virtualroomtype_element.virtual_roomtype_name).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(virtualroomtype_element.virtual_roomtype_name).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(virtualroomtype_element.virtual_roomtype_name).send_keys(typename)
        # 描述
        self.driver.find_element_by_xpath(virtualroomtype_element.beizhu).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(virtualroomtype_element.beizhu).send_keys(beizhu)
        #点击保存
        time.sleep(2)
        self.driver.find_element_by_xpath(virtualroomtype_element.edit_savebutton).click()

    def delete_virtual_roomtype(self):
        #点击删除按钮
        comfunc.wait(self.driver, virtualroomtype_element.delete_virtual_roomtype_button)
        self.driver.find_element_by_xpath(virtualroomtype_element.delete_virtual_roomtype_button).click()
        #点击删除确认按钮
        comfunc.wait(self.driver, virtualroomtype_element.delete_confirm_button)
        self.driver.find_element_by_xpath(virtualroomtype_element.delete_confirm_button).click()

    def delete_assert(self,ele):
        # comfunc.wait_noelement(self.driver, virtualroomtype_element.delete_virtual_roomtype_button)
        comfunc.wait_noelement(self.driver, ele)

    # def batchdelete_virtual_roomtype(self):
    #     #勾选要删除的房型
    #     # comfunc.wait(self.driver, virtualroomtype_element.check_box)
    #     # actions = ActionChains(self.driver)
    #     # actions.click(on_element=virtualroomtype_element.check_box)
    #     # actions.perform()
    #     checkboxs = self.driver.find_elements_by_xpath(virtualroomtype_element.check_box)
    #     print(len(checkboxs))
    #     for a in checkboxs:
    #         if a.get_attribute('value') == '1':
    #             a.click()
    #     #点击批量删除按钮
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath(virtualroomtype_element.batch_delete_button).click()
