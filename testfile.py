'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
print ("加载驱动完成..")
driver.get("http://192.168.10.204/pms/homepage")#加载页面
print ("加载页面完成..")

driver.maximize_window()
 # 登录
driver.find_element_by_id("username").send_keys("autoz")
driver.find_element_by_id('password').send_keys("0123")
driver.find_element_by_id('submit').click()
time.sleep(3)
chain = ActionChains(driver)
chain.move_to_element("//nz-dropdown/div/a")
chain.perform()



# #登录
# driver.find_element_by_id("username").send_keys("autoz")
# driver.find_element_by_id('password').send_keys("0123")
# driver.find_element_by_id('submit').click()
#
# #点击系统
# WebDriverWait(driver,15,0.5).until(
#         EC.presence_of_element_located((By.XPATH, "//a[text()='系统']")))
# driver.find_element_by_xpath("//a[text()='系统']").click()
#
# WebDriverWait(driver,15,0.5).until(
#         EC.presence_of_element_located((By.XPATH, "//p[text()='基础设施']/..")))
# driver.find_element_by_xpath("//p[text()='基础设施']/..").click()
#
# WebDriverWait(driver,15,0.5).until(
#         EC.presence_of_element_located((By.XPATH, "//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='房型维护']")))
# driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='房型维护']").click()
# time.sleep(3)
# a = driver.find_element_by_xpath("//td[text()='单人间']/../td[7]").text
# if a == "启用":
#     print("true")
# else:
#     print("false")
#
