'''
公共方法文件
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def wait(driver,element):
    WebDriverWait(driver,15,0.5).until(
        EC.presence_of_element_located((By.XPATH, element)))

def wait_noelement(driver,element):
    WebDriverWait(driver,10, 0.5).until_not(EC.visibility_of_element_located((By.XPATH, element)))

#将元素滚动到可见区域
def element_scrollIntoView(self,ele):
    self.driver.execute_script("arguments[0].scrollIntoView();", ele)
    time.sleep(0.5)

#等待元素可见
def wait_visibility(driver,element):
    WebDriverWait(driver,10, 0.5).until(
        EC.visibility_of_element_located((By.XPATH, element)))
