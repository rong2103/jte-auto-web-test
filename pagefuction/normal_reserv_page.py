'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import normal_reserve_element
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class NormalReserv:
    def __init__(self,driver):
        self.driver = driver

    #点击团队预订
    def click_teamreservev(self):
        comfunc.wait(self.driver,normal_reserve_element.teamresv_menue)
        self.driver.find_element_by_xpath(normal_reserve_element.teamresv_menue).click()

    #点击长包房预订
    def click_longreservev(self):
        comfunc.wait(self.driver, normal_reserve_element.longresv_menue)
        self.driver.find_element_by_xpath(normal_reserve_element.longresv_menue).click()

    #散客预订
    def individual_normal_reserv(self,reservperson,reservphone):
        #输入预订人
        comfunc.wait(self.driver,normal_reserve_element.resvPerson)
        self.driver.find_element_by_xpath(normal_reserve_element.resvPerson).send_keys(reservperson)
        #输入手机号码
        comfunc.wait(self.driver, normal_reserve_element.reservphone)
        self.driver.find_element_by_xpath(normal_reserve_element.reservphone).send_keys(reservphone)
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
    def not_individual_normal_reserv(self,ele):
        #点击客源类型-单位  normal_reserve_element.customer_type_unit
        comfunc.wait(self.driver, ele)
        self.driver.find_element_by_xpath(ele).click()
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


    #会员调试
    # def not_individual_normal_reserv(self,ele,name):
    #     #点击客源类型-单位  normal_reserve_element.customer_type_unit
    #     comfunc.wait(self.driver, ele)
    #     self.driver.find_element_by_xpath(ele).click()
    #     #点击输入框
    #     time.sleep(1)
    #     comfunc.wait(self.driver, normal_reserve_element.customer_info_input)
    #     # self.driver.find_element_by_xpath(normal_reserve_element.customer_info_input).click()
    #     obj = self.driver.find_element_by_xpath(normal_reserve_element.customer_info_input)
    #     actions = ActionChains(self.driver).click(obj).perform()
    #     self.driver.find_element_by_xpath(normal_reserve_element.input_info).send_keys("a")
    #     time.sleep(1)
    #     # #从输入框下拉列表中选择一个单位点击
    #     # comfunc.wait(self.driver, normal_reserve_element.customer_info_drop_down)
    #     self.driver.find_element_by_xpath(normal_reserve_element.customer_info_drop_down).click()
    #     time.sleep(1.5)
    #     self.driver.find_element_by_xpath(normal_reserve_element.addroomnumber_button).click()
    #     time.sleep(1)
    #     # 点击确定按钮
    #     comfunc.wait(self.driver, normal_reserve_element.submit_button)
    #     self.driver.find_element_by_xpath(normal_reserve_element.submit_button).click()
    #     time.sleep(10)

