'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import unitinfo_datas
from pagefuction.unitinfo_page import UnitInfoPage
from pagefuction.home_page import HomePage
import pytest
import time

@pytest.mark.usefixture("init_env")
class TestRoomInfo:

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_1_add_unitinfo(self,init_env):
        hp = HomePage(init_env)
        hp.click_unit()
        uip = UnitInfoPage(init_env)
        uip.add_unitinfo(unitinfo_datas.new_unit_name,unitinfo_datas.new_contact_person,unitinfo_datas.new_contact_mobile)
        uip.assertadd()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_2_view_unitinfo(self, init_env):
        hp = HomePage(init_env)
        hp.click_unit()
        uip = UnitInfoPage(init_env)
        uip.view_unitinfo()
        uip.view_assert()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_3_modify_unitinfo(self, init_env):
        hp = HomePage(init_env)
        hp.click_unit()
        uip = UnitInfoPage(init_env)
        uip.edit_unitinfo()
        uip.assertadd()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_4_disable_unitinfo(self, init_env):
        hp = HomePage(init_env)
        hp.click_unit()
        uip = UnitInfoPage(init_env)
        uip.disable_unitinfo()
        uip.disable_assert()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_5_enable_unitinfo(self, init_env):
        hp = HomePage(init_env)
        hp.click_unit()
        uip = UnitInfoPage(init_env)
        uip.enable_unitinfo()
        uip.enable_assert()