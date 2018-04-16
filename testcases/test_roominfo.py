'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from pagefuction.login_page import LoginPage
from testdatas import login_datas
from selenium import webdriver
from testdatas import room_info_datas
from pagefuction.system_page import SystemPage
from pagefuction.infra_page import InfraPage
from pagefuction.home_page import HomePage
from pagefuction.roominfo_page import RoomInfoPage
from pageelement import roominfo_element
import pytest
import time

@pytest.mark.usefixture("init_env")
class TestRoomInfo:

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_1_add_roominfo(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_roominfo_menu()
        rip = RoomInfoPage(init_env)
        rip.add_roominfo(room_info_datas.add_roomnumber,room_info_datas.add_innertel,room_info_datas.add_outtel)
        rip.assert_add(roominfo_element.add_savebutton)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_2_edit_roominfo(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_roominfo_menu()
        rip = RoomInfoPage(init_env)
        rip.edit_roominfo(room_info_datas.edit_roomnumber)
        rip.assert_add(roominfo_element.add_savebutton)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_3_delete_roominfo(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_roominfo_menu()
        rip = RoomInfoPage(init_env)
        rip.delete_roominfo(roominfo_element.delete_room_button)
        rip.assert_delete()

    @pytest.fixture
    def init_batch(self):
        option = webdriver.ChromeOptions()
        option.add_argument("test-type")
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome()
        lp = LoginPage(driver)
        lp.login(login_datas.url, login_datas.usr, login_datas.pwd)
        yield driver
        rip = RoomInfoPage(driver)
        #0305
        js = "varq=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        rip.delete_roominfo(roominfo_element.batchadd_delete_button)
        time.sleep(1)
        driver.close()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_4_batchadd_roominfo(self, init_batch):
        hp = HomePage(init_batch)
        hp.click_system()
        sp = SystemPage(init_batch)
        sp.click_infrastructure()
        ip = InfraPage(init_batch)
        ip.click_roominfo_menu()
        rip = RoomInfoPage(init_batch)
        rip.batchadd_roominfo(room_info_datas.batch_add_roomnumber_start,room_info_datas.batch_add_roomnumber_end,room_info_datas.batch_add_phonesub_start,room_info_datas.batch_add_phonesub_end,room_info_datas.batch_add_phoneout_start,room_info_datas.batch_add_phoneout_end)
        rip.assert_batchadd()
        #删除批量新增的房间
        # rip.delete_roominfo(roominfo_element.batchadd_delete_button)


    # @pytest.mark.test
    # @pytest.mark.smoke
    # def test_4_batchadd_roominfo(self, init_env):
    #     hp = HomePage(init_env)
    #     hp.click_system()
    #     sp = SystemPage(init_env)
    #     sp.click_infrastructure()
    #     ip = InfraPage(init_env)
    #     ip.click_roominfo_menu()
    #     rip = RoomInfoPage(init_env)
    #     rip.batchadd_roominfo(room_info_datas.batch_add_roomnumber_start,room_info_datas.batch_add_roomnumber_end,room_info_datas.batch_add_phonesub_start,room_info_datas.batch_add_phonesub_end,room_info_datas.batch_add_phoneout_start,room_info_datas.batch_add_phoneout_end)
    #     rip.assert_batchadd()
    #     #删除批量新增的房间
    #     # rip.delete_roominfo(roominfo_element.batchadd_delete_button)
