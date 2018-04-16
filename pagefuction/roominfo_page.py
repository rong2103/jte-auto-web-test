'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import roominfo_element
import time
from selenium.webdriver.common.keys import Keys

class RoomInfoPage:
    def __init__(self,driver):
        self.driver = driver

    def add_roominfo(self,roomnumber,innerTel,outTel):
        #点击新增按钮
        comfunc.wait(self.driver, roominfo_element.add_room_button)
        self.driver.find_element_by_xpath(roominfo_element.add_room_button).click()
        #输入界面字段
        #楼层
        comfunc.wait(self.driver, roominfo_element.add_floor_select)
        self.driver.find_element_by_xpath(roominfo_element.add_floor_select).click()
        time.sleep(2)
        comfunc.wait(self.driver, roominfo_element.add_floor_value)
        self.driver.find_element_by_xpath(roominfo_element.add_floor_value).click()
        #房型
        comfunc.wait(self.driver, roominfo_element.add_roomtype_select)
        self.driver.find_element_by_xpath(roominfo_element.add_roomtype_select).click()
        time.sleep(2)
        comfunc.wait(self.driver, roominfo_element.add_roomtype_value)
        self.driver.find_element_by_xpath(roominfo_element.add_roomtype_value).click()
        #房间号
        self.driver.find_element_by_xpath(roominfo_element.add_room_number).send_keys(roomnumber)
        self.driver.find_element_by_xpath(roominfo_element.add_room_innerTel).send_keys(innerTel)
        self.driver.find_element_by_xpath(roominfo_element.add_room_outTel).send_keys(outTel)
        #保存
        self.driver.find_element_by_xpath(roominfo_element.add_savebutton).click()

    def assert_add(self,ele):
        comfunc.wait_noelement(self.driver,ele)

    def edit_roominfo(self,roomnumber):
        #点击修改按钮
        comfunc.wait(self.driver, roominfo_element.edit_room_button)
        self.driver.find_element_by_xpath(roominfo_element.edit_room_button).click()
        #输入界面字段
        # #楼层
        # comfunc.wait(self.driver, roominfo_element.add_floor_select)
        # self.driver.find_element_by_xpath(roominfo_element.add_floor_select).click()
        # time.sleep(2)
        # comfunc.wait(self.driver, roominfo_element.add_floor_value)
        # self.driver.find_element_by_xpath(roominfo_element.add_floor_value).click()
        # #房型
        # comfunc.wait(self.driver, roominfo_element.add_roomtype_select)
        # self.driver.find_element_by_xpath(roominfo_element.add_roomtype_select).click()
        # time.sleep(2)
        # comfunc.wait(self.driver, roominfo_element.add_roomtype_value)
        # self.driver.find_element_by_xpath(roominfo_element.add_roomtype_value).click()
        #房间号
        comfunc.wait(self.driver, roominfo_element.add_room_number)
        self.driver.find_element_by_xpath(roominfo_element.add_room_number).click()
        self.driver.find_element_by_xpath(roominfo_element.add_room_number).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(roominfo_element.add_room_number).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(roominfo_element.add_room_number).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(roominfo_element.add_room_number).send_keys(roomnumber)
        # self.driver.find_element_by_xpath(roominfo_element.add_room_innerTel).send_keys(innerTel)
        # self.driver.find_element_by_xpath(roominfo_element.add_room_outTel).send_keys(outTel)
        #保存按钮
        self.driver.find_element_by_xpath(roominfo_element.add_savebutton).click()

    def delete_roominfo(self,ele):
        #点击删除按钮
        comfunc.wait(self.driver, ele)
        self.driver.find_element_by_xpath(ele).click()
        comfunc.wait(self.driver, roominfo_element.delete_confirm_button)
        self.driver.find_element_by_xpath(roominfo_element.delete_confirm_button).click()

    def assert_delete(self):
        comfunc.wait_noelement(self.driver, roominfo_element.delete_room_button)


    def batchadd_roominfo(self,roomnumberstart,roomnumberend,innerstart,innerend,outstart,outend):
        #点击批量新增按钮
        comfunc.wait(self.driver, roominfo_element.batch_add_button)
        self.driver.find_element_by_xpath(roominfo_element.batch_add_button).click()
        #输入界面字段
        #楼层
        comfunc.wait(self.driver, roominfo_element.add_floor_select)
        self.driver.find_element_by_xpath(roominfo_element.add_floor_select).click()
        time.sleep(2)
        comfunc.wait(self.driver, roominfo_element.add_floor_value)
        self.driver.find_element_by_xpath(roominfo_element.add_floor_value).click()
        #房型
        comfunc.wait(self.driver, roominfo_element.add_roomtype_select)
        self.driver.find_element_by_xpath(roominfo_element.add_roomtype_select).click()
        time.sleep(2)
        comfunc.wait(self.driver, roominfo_element.add_roomtype_value)
        self.driver.find_element_by_xpath(roominfo_element.add_roomtype_value).click()
        #房间号开始
        self.driver.find_element_by_xpath(roominfo_element.batchadd_roomnumber_start).send_keys(roomnumberstart)
        #房间号结束
        self.driver.find_element_by_xpath(roominfo_element.batchadd_roomnumber_end).send_keys(roomnumberend)
        #电话分机开始
        self.driver.find_element_by_xpath(roominfo_element.batchadd_phonesub_start).send_keys(innerstart)
        #电话分机结束
        self.driver.find_element_by_xpath(roominfo_element.batchadd_phonesub_end).send_keys(innerend)
        #电话外线开始
        self.driver.find_element_by_xpath(roominfo_element.batchadd_phoneout_start).send_keys(outstart)
        #电话外线结束
        self.driver.find_element_by_xpath(roominfo_element.batchadd_phoneout_end).send_keys(outend)

        #保存
        self.driver.find_element_by_xpath(roominfo_element.batchadd_savebutton).click()

    def assert_batchadd(self):
        comfunc.wait(self.driver, roominfo_element.batchadd_delete_button)
        # comfunc.wait_noelement(self.driver,roominfo_element.batchadd_roomnumber_start)