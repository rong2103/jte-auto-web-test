'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import virtual_roomtype_datas
from pagefuction.system_page import SystemPage
from pagefuction.infra_page import InfraPage
from pagefuction.home_page import HomePage
from pagefuction.virtual_roomtype_page import VirtualRoomTypePage
from pageelement import virtualroomtype_element
import pytest
import time

@pytest.mark.usefixture("init_env")
class TestVirtualRoomType:

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_1_add_virtualroomtype(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_virtual_roomtype_menu()
        vrtp = VirtualRoomTypePage(init_env)
        vrtp.add_virtual_roomtype(virtual_roomtype_datas.virtual_roomtype_name,virtual_roomtype_datas.beizhu)
        vrtp.assert_add(virtualroomtype_element.virtual_roomtype_name)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_2_edit_virtualroomtype(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_virtual_roomtype_menu()
        vrtp = VirtualRoomTypePage(init_env)
        vrtp.edit_virtual_roomtype(virtual_roomtype_datas.edit_roomtype_name, virtual_roomtype_datas.edit_beizhu)
        vrtp.assert_add(virtualroomtype_element.virtual_roomtype_name)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_3_delete_virtualroomtype(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_virtual_roomtype_menu()
        vrtp = VirtualRoomTypePage(init_env)
        vrtp.delete_virtual_roomtype()
        vrtp.delete_assert(virtualroomtype_element.delete_virtual_roomtype_button)

    # @pytest.mark.test
    # def test_4_batchdelete_virtualroomtype(self, init_env):
    #     hp = HomePage(init_env)
    #     hp.click_system()
    #     sp = SystemPage(init_env)
    #     sp.click_infrastructure()
    #     ip = InfraPage(init_env)
    #     ip.click_virtual_roomtype_menu()
    #     vrtp = VirtualRoomTypePage(init_env)
    #     vrtp.add_virtual_roomtype(virtual_roomtype_datas.batch_virtual_roomtype,virtual_roomtype_datas.batch_beizhu)
    #     time.sleep(2)
    #     vrtp.batchdelete_virtual_roomtype()
    #     vrtp.delete_assert(virtualroomtype_element.check_box)
