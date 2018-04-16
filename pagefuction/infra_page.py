'''
基础设施模块的方法文件
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-

from common import comfunc
from pageelement import infra_element
import time
from selenium.webdriver.common.keys import Keys

class InfraPage:

    def __init__(self,driver):
        self.driver = driver

    # def log(self):
    #     print("building_group")
    #     print(self.building_group)

    #新增楼栋
    def add_building(self,new_buildname,new_buildremark):
        comfunc.wait(self.driver,infra_element.addbuilding_button)
        #点击新增楼栋按钮
        self.driver.find_element_by_xpath(infra_element.addbuilding_button).click()
        comfunc.wait(self.driver,infra_element.buildingname_input)
        comfunc.wait(self.driver, infra_element.remark_input)
        self.driver.find_element_by_xpath(infra_element.buildingname_input).send_keys(new_buildname)
        self.driver.find_element_by_xpath(infra_element.remark_input).send_keys(new_buildremark)
        comfunc.wait(self.driver, infra_element.savebuilding_button)
        self.driver.find_element_by_xpath(infra_element.savebuilding_button).click()

    def new_build_assert(self):
        #return self.driver.find_element_by_xpath(self.building_group).text
        comfunc.wait(self.driver,infra_element.new_building_group)

    # 修改楼栋
    def edit_building(self, edit_buildname, edit_buildremark):
        #等待新增的楼栋显示
        comfunc.wait(self.driver, infra_element.new_building_group)
        # 点击新增的楼栋
        self.driver.find_element_by_xpath(infra_element.new_building_group).click()
        #点击修改按钮
        self.driver.find_element_by_xpath(infra_element.build_edit_button).click()
        comfunc.wait(self.driver, infra_element.edit_build_name)
        comfunc.wait(self.driver, infra_element.edit_build_remark)
        #修改楼栋名
        # self.driver.find_element_by_xpath(infra_element.edit_build_name).clear()
        self.driver.find_element_by_xpath(infra_element.edit_build_name).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(infra_element.edit_build_name).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(infra_element.edit_build_name).send_keys(edit_buildname)
        #修改楼栋备注
        self.driver.find_element_by_xpath(infra_element.edit_build_remark).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(infra_element.edit_build_remark).send_keys(edit_buildremark)
        comfunc.wait(self.driver, infra_element.edit_build_savebutton)
        self.driver.find_element_by_xpath(infra_element.edit_build_savebutton).click()

    def edit_build_assert(self):
        #return self.driver.find_element_by_xpath(self.building_group).text
        comfunc.wait(self.driver,infra_element.edit_building_group)


    def add_floor(self,new_startfloor,new_endfloor,new_floor_remark):
        #点击要新增楼层的楼栋
        comfunc.wait(self.driver,infra_element.edit_building_group)
        self.driver.find_element_by_xpath(infra_element.edit_building_group).click()
        #点击新增楼层按钮
        comfunc.wait(self.driver,infra_element.add_floor_button)
        self.driver.find_element_by_xpath(infra_element.add_floor_button).click()
        #输入楼层数据
        comfunc.wait(self.driver, infra_element.addfloor_startfloor_input)
        comfunc.wait(self.driver, infra_element.addfloor_endfloor_input)
        comfunc.wait(self.driver, infra_element.addfloor_remark)
        self.driver.find_element_by_xpath(infra_element.addfloor_startfloor_input).send_keys(new_startfloor)
        time.sleep(1.5)
        self.driver.find_element_by_xpath(infra_element.addfloor_endfloor_input).send_keys(new_endfloor)
        self.driver.find_element_by_xpath(infra_element.addfloor_remark).send_keys(new_floor_remark)
        time.sleep(1)
        self.driver.find_element_by_xpath(infra_element.addfloor_savebutton).click()

    def add_floor_assert(self):
        time.sleep(1.5)
        comfunc.wait(self.driver,infra_element.edit_building_group)
        self.driver.find_element_by_xpath(infra_element.edit_building_group).click()
        comfunc.wait(self.driver, infra_element.newfloor_inlist)

    def edit_floor(self,floor,floor_remark):
        #点击要修改楼层的楼栋
        comfunc.wait(self.driver,infra_element.edit_building_group)
        self.driver.find_element_by_xpath(infra_element.edit_building_group).click()
        #选择要修改的楼层
        time.sleep(1)
        self.driver.find_element_by_xpath(infra_element.newfloor_inlist).click()
        #点击修改按钮
        comfunc.wait(self.driver,infra_element.floor_edit_button)
        self.driver.find_element_by_xpath(infra_element.floor_edit_button).click()
        #输入楼层数据
        comfunc.wait(self.driver, infra_element.edit_floor_input)
        comfunc.wait(self.driver, infra_element.edit_floor_remark)
        self.driver.find_element_by_xpath(infra_element.edit_floor_input).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(infra_element.edit_floor_input).clear()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(infra_element.edit_floor_input).send_keys(floor)
        self.driver.find_element_by_xpath(infra_element.edit_floor_remark).clear()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(infra_element.edit_floor_remark).send_keys(floor_remark)
        comfunc.wait(self.driver, infra_element.edit_floor_savebutton)
        self.driver.find_element_by_xpath(infra_element.edit_floor_savebutton).click()

    def edit_floor_assert(self):
        time.sleep(1)
        comfunc.wait(self.driver, infra_element.edit_building_group)
        self.driver.find_element_by_xpath(infra_element.edit_building_group).click()
        comfunc.wait(self.driver, infra_element.editfloor_inlist)

    def delete_floor(self):
        #点击要删除楼层的楼栋
        comfunc.wait(self.driver,infra_element.edit_building_group)
        self.driver.find_element_by_xpath(infra_element.edit_building_group).click()
        #选择要删除的楼层
        time.sleep(1)
        self.driver.find_element_by_xpath(infra_element.editfloor_inlist).click()
        #点击删除按钮
        comfunc.wait(self.driver,infra_element.floor_delete_button)
        self.driver.find_element_by_xpath(infra_element.floor_delete_button).click()
        comfunc.wait(self.driver,infra_element.floor_delete_confirm_button)
        self.driver.find_element_by_xpath(infra_element.floor_delete_confirm_button).click()

    def delete_building(self):
        #点击要删除楼栋的楼栋
        comfunc.wait(self.driver,infra_element.edit_building_group)
        self.driver.find_element_by_xpath(infra_element.edit_building_group).click()
        #点击删除按钮
        comfunc.wait(self.driver,infra_element.build_delete_button)
        self.driver.find_element_by_xpath(infra_element.build_delete_button).click()
        comfunc.wait(self.driver,infra_element.build_delete_confirm_button)
        self.driver.find_element_by_xpath(infra_element.build_delete_confirm_button).click()

    def delete_build_assert(self):
        time.sleep(1)
        comfunc.wait_noelement(self.driver,infra_element.edit_building_group)

    def delete_floor_assert(self):
        time.sleep(1)
        comfunc.wait_noelement(self.driver,infra_element.editfloor_inlist)

    #点击房型维护菜单
    def click_room_maintain(self):
        comfunc.wait(self.driver, infra_element.room_maintain_menu)
        self.driver.find_element_by_xpath(infra_element.room_maintain_menu).click()

    #点击虚拟房型菜单
    def click_virtual_roomtype_menu(self):
        comfunc.wait(self.driver, infra_element.virtual_roomtype_menu)
        self.driver.find_element_by_xpath(infra_element.virtual_roomtype_menu).click()

    #点击房间信息菜单
    def click_roominfo_menu(self):
        comfunc.wait(self.driver, infra_element.room_info_menu)
        self.driver.find_element_by_xpath(infra_element.room_info_menu).click()

    #点击门锁维护菜单
    def click_roomlock_menu(self):
        comfunc.wait(self.driver, infra_element.roomlock_maintain_menu)
        self.driver.find_element_by_xpath(infra_element.roomlock_maintain_menu).click()

