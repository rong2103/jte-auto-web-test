'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import room_maintain_datas
from pagefuction.system_page import SystemPage
from pagefuction.infra_page import InfraPage
from pagefuction.home_page import HomePage
from pagefuction.roomtype_maintain_page import RoomMaintainPage
from pageelement import roomtype_maintain_element
import pytest

@pytest.mark.usefixture("init_env")
class TestRoomMaintain:

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_1_add_roomtype(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_room_maintain()
        rmp = RoomMaintainPage(init_env)
        rmp.add_roomtype(room_maintain_datas.roomtype_name,room_maintain_datas.availableNumber,room_maintain_datas.deposit,room_maintain_datas.alias,room_maintain_datas.price,room_maintain_datas.exceedReserveNumber,room_maintain_datas.beizhu)
        rmp.assert_add(roomtype_maintain_element.roomtype_name)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_2_edit_roomtype(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_room_maintain()
        rmp = RoomMaintainPage(init_env)
        rmp.edit_roomtype(room_maintain_datas.edit_roomtype_name,room_maintain_datas.edit_beizhu)
        rmp.assert_add(roomtype_maintain_element.roomtype_name)

    #禁用
    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_3_disable_roomtype(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_room_maintain()
        rmp = RoomMaintainPage(init_env)
        rmp.disable_roomtype()
        rmp.disable_assert()

    #启用
    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_4_enable_roomtype(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_room_maintain()
        rmp = RoomMaintainPage(init_env)
        rmp.enable_roomtype()
        rmp.enable_assert()


    #删除
    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_5_delete_roomtype(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.click_room_maintain()
        rmp = RoomMaintainPage(init_env)
        rmp.delete_roomtype()
        rmp.assert_delete(roomtype_maintain_element.delete_button)