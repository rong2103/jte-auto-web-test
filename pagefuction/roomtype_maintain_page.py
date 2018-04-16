'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import infra_element
from pageelement import roomtype_maintain_element
import time

class RoomMaintainPage:
    def __init__(self,driver):
        self.driver = driver

    def add_roomtype(self,typename,availablenumber,deposit,alias,price,exceedReserveNumber,beizhu):
        #点击新增按钮
        comfunc.wait(self.driver, roomtype_maintain_element.add_roomtype_button)
        self.driver.find_element_by_xpath(roomtype_maintain_element.add_roomtype_button).click()
        #输入界面字段
        #房型
        comfunc.wait(self.driver, roomtype_maintain_element.roomtype_name)
        self.driver.find_element_by_xpath(roomtype_maintain_element.roomtype_name).send_keys(typename)
        #可入住数
        comfunc.wait(self.driver, roomtype_maintain_element.availableNumber)
        self.driver.find_element_by_xpath(roomtype_maintain_element.availableNumber).send_keys(availablenumber)
        #押金
        comfunc.wait(self.driver, roomtype_maintain_element.deposit)
        self.driver.find_element_by_xpath(roomtype_maintain_element.deposit).send_keys(deposit)
        #简称
        comfunc.wait(self.driver, roomtype_maintain_element.alias)
        self.driver.find_element_by_xpath(roomtype_maintain_element.alias).send_keys(alias)
        #门市价
        comfunc.wait(self.driver, roomtype_maintain_element.price)
        self.driver.find_element_by_xpath(roomtype_maintain_element.price).send_keys(price)
        #超预订数
        comfunc.wait(self.driver, roomtype_maintain_element.exceedReserveNumber)
        self.driver.find_element_by_xpath(roomtype_maintain_element.exceedReserveNumber).send_keys(exceedReserveNumber)
        #备注
        comfunc.wait(self.driver, roomtype_maintain_element.beizhu)
        self.driver.find_element_by_xpath(roomtype_maintain_element.beizhu).send_keys(beizhu)
        #点击保存按钮
        self.driver.find_element_by_xpath(roomtype_maintain_element.savebutton).click()

    def assert_add(self,element):
        comfunc.wait_noelement(self.driver, element)

    def edit_roomtype(self,typename,beizhu):
        #点击修改按钮
        comfunc.wait(self.driver, roomtype_maintain_element.modify_button)
        self.driver.find_element_by_xpath(roomtype_maintain_element.modify_button).click()
        #输入界面字段
        #房型
        comfunc.wait(self.driver, roomtype_maintain_element.roomtype_name)
        self.driver.find_element_by_xpath(roomtype_maintain_element.roomtype_name).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(roomtype_maintain_element.roomtype_name).send_keys(typename)
        # #可入住数
        # comfunc.wait(self.driver, room_maintain_element.availableNumber)
        # self.driver.find_element_by_xpath(room_maintain_element.availableNumber).send_keys(availablenumber)
        # #押金
        # comfunc.wait(self.driver, room_maintain_element.deposit)
        # self.driver.find_element_by_xpath(room_maintain_element.deposit).send_keys(deposit)
        # #简称
        # comfunc.wait(self.driver, room_maintain_element.alias)
        # self.driver.find_element_by_xpath(room_maintain_element.alias).send_keys(alias)
        # #门市价
        # comfunc.wait(self.driver, room_maintain_element.price)
        # self.driver.find_element_by_xpath(room_maintain_element.price).send_keys(price)
        # #超预订数
        # comfunc.wait(self.driver, room_maintain_element.exceedReserveNumber)
        # self.driver.find_element_by_xpath(room_maintain_element.exceedReserveNumber).send_keys(exceedReserveNumber)
        #备注
        comfunc.wait(self.driver, roomtype_maintain_element.beizhu)
        self.driver.find_element_by_xpath(roomtype_maintain_element.beizhu).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(roomtype_maintain_element.beizhu).send_keys(beizhu)
        #点击保存按钮
        self.driver.find_element_by_xpath(roomtype_maintain_element.savebutton).click()

    def disable_roomtype(self):
        #点击禁用按钮
        comfunc.wait(self.driver, roomtype_maintain_element.disable_button)
        self.driver.find_element_by_xpath(roomtype_maintain_element.disable_button).click()

    def disable_assert(self):
        # comfunc.wait(self.driver, roomtype_maintain_element.status)将这句改成下面的固定时间等待之后用例执行成功
        time.sleep(2)
        # print(roomtype_maintain_element.status)
        a = self.driver.find_element_by_xpath(roomtype_maintain_element.status).text
        # print(a)
        # print(type(a))
        assert a == "禁用"

    #启用
    def enable_roomtype(self):
        #点击禁用按钮
        comfunc.wait(self.driver, roomtype_maintain_element.disable_button)
        self.driver.find_element_by_xpath(roomtype_maintain_element.disable_button).click()

    def enable_assert(self):
        # comfunc.wait(self.driver, roomtype_maintain_element.status)
        time.sleep(2)
        a = self.driver.find_element_by_xpath(roomtype_maintain_element.status).text
        assert a == "启用"

    def delete_roomtype(self):
        #点击删除按钮
        comfunc.wait(self.driver, roomtype_maintain_element.delete_button)
        self.driver.find_element_by_xpath(roomtype_maintain_element.delete_button).click()
        #点击删除确认按钮
        comfunc.wait(self.driver, roomtype_maintain_element.delete_confirm_button)
        self.driver.find_element_by_xpath(roomtype_maintain_element.delete_confirm_button).click()

    def assert_delete(self,element):
        comfunc.wait_noelement(self.driver,element)
