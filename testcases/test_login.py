'''
登录用例测试文件
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from pagefuction.login_page import LoginPage
from pagefuction.home_page import HomePage
from testdatas import login_datas

@pytest.mark.usefixture("login_init")
class TestLogin:

    def test_login_success(self,login_init):
        #lp = LoginPage(login_init[0])
        login_init[1].login(login_datas.url,login_datas.usr,login_datas.pwd)

        hp = HomePage(login_init[0])
        try:
            hp.exist_homepagebutton()
        except Exception as e:
            login_init[2].append(e)
            #self.assertEqual([],e)
            assert [] == e


