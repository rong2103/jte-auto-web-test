'''
首页操作方法
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageelement import home_element

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    def exist_homepagebutton(self):
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH,home_element.homepage_button_locator)))

    #点击系统菜单
    def click_system(self):
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.XPATH, home_element.menu_system)))
        self.driver.find_element_by_xpath(home_element.menu_system).click()

    # 点击预订菜单
    def click_reserv(self):
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.XPATH, home_element.menu_reserv)))
        self.driver.find_element_by_xpath(home_element.menu_reserv).click()

    # 点击入住菜单
    def click_checkin(self):
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.XPATH, home_element.menu_checkin)))
        self.driver.find_element_by_xpath(home_element.menu_checkin).click()

    # 点击会员菜单
    def click_member(self):
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.XPATH, home_element.menu_member)))
        self.driver.find_element_by_xpath(home_element.menu_member).click()

    # 点击单位菜单
    def click_unit(self):
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.XPATH, home_element.menu_unit)))
        self.driver.find_element_by_xpath(home_element.menu_unit).click()

    # 点击中介菜单
    def click_intermediary(self):
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.XPATH, home_element.menu_intermediary)))
        self.driver.find_element_by_xpath(home_element.menu_intermediary).click()

    # 点击市场活动菜单
    def click_(self):
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.XPATH, home_element.menu_market)))
        self.driver.find_element_by_xpath(home_element.menu_market).click()

    # 点击房间菜单
    def click_marketroom(self):
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.XPATH, home_element.menu_room)))
        self.driver.find_element_by_xpath(home_element.menu_room).click()

    # 点击库存菜单
    def click_storage(self):
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.XPATH, home_element.menu_storage)))
        self.driver.find_element_by_xpath(home_element.menu_storage).click()


