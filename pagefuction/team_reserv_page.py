'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import normal_reserve_element
import time

class TeamReserve:
    def __init__(self,driver):
        self.driver = driver

    #散客预订
    def individual_normal_reserv(self,reservperson,reservphone,teamname):
        #输入预订人
        comfunc.wait(self.driver,normal_reserve_element.resvPerson)
        self.driver.find_element_by_xpath(normal_reserve_element.resvPerson).send_keys(reservperson)
        #输入手机号码
        comfunc.wait(self.driver, normal_reserve_element.reservphone)
        self.driver.find_element_by_xpath(normal_reserve_element.reservphone).send_keys(reservphone)
        #输入团名
        comfunc.wait(self.driver, normal_reserve_element.team_name_input)
        self.driver.find_element_by_xpath(normal_reserve_element.team_name_input).send_keys(teamname)
        # #增加房间个数
        # comfunc.wait(self.driver, normal_reserve_element.addroomnumber_button)
        # self.driver.find_element_by_xpath(normal_reserve_element.addroomnumber_button).click()
        #选择房型
        comfunc.wait(self.driver, normal_reserve_element.addroomnumber_button)
        self.driver.find_element_by_xpath(normal_reserve_element.addroomnumber_button).click()
        time.sleep(1)
        #选择房间号
        comfunc.wait(self.driver, normal_reserve_element.select_roomnumber)
        self.driver.find_element_by_xpath(normal_reserve_element.select_roomnumber).click()
        # 点击确定按钮
        comfunc.wait(self.driver, normal_reserve_element.submit_button)
        self.driver.find_element_by_xpath(normal_reserve_element.submit_button).click()

    def is_exist_ele(self,ele):
        comfunc.wait(self.driver, ele)

    # 单位中介
    def not_individual_normal_reserv(self,ele,teamname):
        #点击客源类型-单位  normal_reserve_element.customer_type_unit
        comfunc.wait(self.driver, ele)
        self.driver.find_element_by_xpath(ele).click()
        # 输入团名
        comfunc.wait(self.driver, normal_reserve_element.team_name_input)
        self.driver.find_element_by_xpath(normal_reserve_element.team_name_input).send_keys(teamname)
        #点击输入框
        time.sleep(1)
        comfunc.wait(self.driver, normal_reserve_element.customer_info_input)
        self.driver.find_element_by_xpath(normal_reserve_element.customer_info_input).click()
        time.sleep(1)
        # #从输入框下拉列表中选择一个单位点击
        # comfunc.wait(self.driver, normal_reserve_element.customer_info_drop_down)
        self.driver.find_element_by_xpath(normal_reserve_element.customer_info_drop_down).click()
        time.sleep(1.5)
        self.driver.find_element_by_xpath(normal_reserve_element.addroomnumber_button).click()
        time.sleep(1)
        # 点击确定按钮
        comfunc.wait(self.driver, normal_reserve_element.submit_button)
        self.driver.find_element_by_xpath(normal_reserve_element.submit_button).click()
        time.sleep(10)