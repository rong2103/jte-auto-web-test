'''
测试用例公共fixture文件
__author__ = ‘zhourong‘
'''

from pagefuction.login_page import LoginPage
from testdatas import login_datas
from selenium import webdriver
import pytest

@pytest.fixture()
def login_init():
    option = webdriver.ChromeOptions()
    option.add_argument("test-type")
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()
    lp = LoginPage(driver)
    verificationErrors = []
    yield [driver,lp,verificationErrors]    #yield后面是返回值列表
    driver.close()

@pytest.fixture()
def init_env():
    option = webdriver.ChromeOptions()
    option.add_argument("test-type")
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login(login_datas.url,login_datas.usr,login_datas.pwd)
    yield driver
    driver.close()