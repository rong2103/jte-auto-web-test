'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageelement import login_element

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def login(self,url,username,password):
        #等待元素出现
        self.driver.get(url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 3, 0.5).until(EC.presence_of_element_located((By.ID, login_element.login_username_locator_id)))
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.ID, login_element.login_password_locator_id)))
        WebDriverWait(self.driver, 3, 0.5).until(
            EC.presence_of_element_located((By.ID, login_element.login_button_locator_id)))

        self.driver.find_element_by_id(login_element.login_username_locator_id).send_keys(username)
        self.driver.find_element_by_id(login_element.login_password_locator_id).send_keys(password)
        self.driver.find_element_by_id(login_element.login_button_locator_id).click()
