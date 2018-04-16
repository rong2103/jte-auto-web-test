'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from common import comfunc
from pageelement import unitinfo_element
from testdatas import unitinfo_datas
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class UnitInfoPage:
    def __init__(self,driver):
        self.driver = driver

    #新增单位信息
    def add_unitinfo(self,unitname,contactperson,mobile):
        #点击新增按钮
        comfunc.wait(self.driver,unitinfo_element.add_button)
        self.driver.find_element_by_xpath(unitinfo_element.add_button).click()
        #输入单位名/联系人/电话
        comfunc.wait(self.driver,unitinfo_element.new_name)
        comfunc.wait(self.driver,unitinfo_element.new_charging_rule_select)
        comfunc.wait(self.driver,unitinfo_element.new_contact_person)
        self.driver.find_element_by_xpath(unitinfo_element.new_name).send_keys(unitname)
        self.driver.find_element_by_xpath(unitinfo_element.new_contact_person).send_keys(contactperson)
        self.driver.find_element_by_xpath(unitinfo_element.new_phone).send_keys(mobile)
        #选择价格策略
        self.driver.find_element_by_xpath(unitinfo_element.new_price_strage_select).click()
        comfunc.wait(self.driver,unitinfo_element.new_price_strage_value)
        self.driver.find_element_by_xpath(unitinfo_element.new_price_strage_value).click()
        time.sleep(1)
        #选择计费规则
        self.driver.find_element_by_xpath(unitinfo_element.new_charging_rule_select).click()
        comfunc.wait(self.driver,unitinfo_element.new_charging_rule_value)
        self.driver.find_element_by_xpath(unitinfo_element.new_charging_rule_value).click()
        #点击保存
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.saveButton).click()
        time.sleep(5)

    def assertadd(self):
        comfunc.wait_noelement(self.driver,unitinfo_datas.new_unit_name)

    #查看详情
    def view_unitinfo(self):
        # 点击详情按钮
        comfunc.wait(self.driver, unitinfo_element.detail_button)
        self.driver.find_element_by_xpath(unitinfo_element.detail_button).click()
        time.sleep(5)

    def view_assert(self):
        comfunc.wait(self.driver,unitinfo_element.view_toprow)
        comfunc.wait(self.driver,unitinfo_element.view_unitname)

    #修改单位信息
    def edit_unitinfo(self):
        #点击修改按钮
        comfunc.wait(self.driver,unitinfo_element.modify_button)
        self.driver.find_element_by_xpath(unitinfo_element.modify_button).click()
        comfunc.wait(self.driver,unitinfo_element.new_charging_rule_select)
        #单位名
        comfunc.wait(self.driver, unitinfo_element.new_name)
        self.driver.find_element_by_xpath(unitinfo_element.new_name).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.new_name).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.new_name).send_keys(unitinfo_datas.edit_unitname)
        #联系人
        comfunc.wait(self.driver, unitinfo_element.new_contact_person)
        self.driver.find_element_by_xpath(unitinfo_element.new_contact_person).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.new_contact_person).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.new_contact_person).send_keys(unitinfo_datas.edit_contact_person)
        #手机
        self.driver.find_element_by_xpath(unitinfo_element.new_phone).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.new_phone).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.new_phone).send_keys(unitinfo_datas.edit_contact_mobile)
        #价格策略
        self.driver.find_element_by_xpath(unitinfo_element.new_price_strage_select).click()
        comfunc.wait(self.driver, unitinfo_element.new_price_strage_value)
        self.driver.find_element_by_xpath(unitinfo_element.new_price_strage_value).click()
        time.sleep(1)
        #计费规则
        self.driver.find_element_by_xpath(unitinfo_element.new_charging_rule_select).click()
        comfunc.wait(self.driver, unitinfo_element.new_charging_rule_value)
        self.driver.find_element_by_xpath(unitinfo_element.new_charging_rule_value).click()
        #挂账额度
        self.driver.find_element_by_xpath(unitinfo_element.debitAmount).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.debitAmount).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.debitAmount).send_keys(unitinfo_datas.edit_debitAmount)
        #早餐券数
        self.driver.find_element_by_xpath(unitinfo_element.couponNumber).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.couponNumber).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.couponNumber).send_keys(unitinfo_datas.edit_couponNumber)
        #银行账号
        self.driver.find_element_by_xpath(unitinfo_element.bankAccount).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.bankAccount).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.bankAccount).send_keys(unitinfo_datas.edit_bankAccount)
        #税号
        self.driver.find_element_by_xpath(unitinfo_element.dutyParagraph).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.dutyParagraph).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.dutyParagraph).send_keys(unitinfo_datas.edit_dutyParagraph)
        #电话
        self.driver.find_element_by_xpath(unitinfo_element.telephone).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.telephone).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.telephone).send_keys(unitinfo_datas.edit_telephone)
        #合同号
        self.driver.find_element_by_xpath(unitinfo_element.agreementNo).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.agreementNo).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.agreementNo).send_keys(unitinfo_datas.edit_agreementNo)
        #邮箱
        self.driver.find_element_by_xpath(unitinfo_element.email).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.email).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.email).send_keys(unitinfo_datas.edit_email)
        #地址
        self.driver.find_element_by_xpath(unitinfo_element.address).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.address).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.address).send_keys(unitinfo_datas.edit_address)
        #备注
        self.driver.find_element_by_xpath(unitinfo_element.remark).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(unitinfo_element.remark).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.remark).send_keys(unitinfo_datas.edit_remark)
        # 点击保存
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.saveButton).click()
        time.sleep(5)

    #禁用
    def disable_unitinfo(self):
        comfunc.wait(self.driver,unitinfo_element.more_button)
        obj = self.driver.find_element_by_xpath(unitinfo_element.more_button)
        ac = ActionChains(self.driver).move_to_element(obj).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.disable_button).click()
        time.sleep(5)

    #启用
    def enable_unitinfo(self):
        comfunc.wait(self.driver,unitinfo_element.more_button)
        obj = self.driver.find_element_by_xpath(unitinfo_element.more_button)
        ac = ActionChains(self.driver).move_to_element(obj).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(unitinfo_element.disable_button).click()
        time.sleep(5)

    def disable_assert(self):
        time.sleep(2)
        # print(roomtype_maintain_element.status)
        a = self.driver.find_element_by_xpath(unitinfo_element.status).text
        assert a.find("禁用")

    def enable_assert(self):
        time.sleep(2)
        # print(roomtype_maintain_element.status)
        a = self.driver.find_element_by_xpath(unitinfo_element.status).text
        assert a.find("启用")






