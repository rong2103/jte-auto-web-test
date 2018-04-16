'''
楼栋楼层模块测试用例文件
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-

from testdatas import infra_datas
from pagefuction.system_page import SystemPage
from pagefuction.infra_page import InfraPage
from pagefuction.home_page import HomePage
from common import comfunc
import pytest

@pytest.mark.usefixture("init_env")
class TestBuildFloor:

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_1_add_build(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.add_building(infra_datas.new_building_name,infra_datas.new_building_remark)
        # ip.wait_newbuild_alert_disappear()
        #assert ip.build_is_exist() == infra_datas.new_building_name
        # ip.log()
        ip.new_build_assert()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_2_edit_build(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.edit_building(infra_datas.edit_building_name,infra_datas.edit_building_remark)
        ip.edit_build_assert()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_3_add_floor(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.add_floor(infra_datas.add_startfloor,infra_datas.add_endfloor,infra_datas.add_floor_remark)
        ip.add_floor_assert()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_4_edit_floor(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.edit_floor(infra_datas.edit_floor,infra_datas.edit_floor_remark)
        ip.edit_floor_assert()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_5_delete_floor(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.delete_floor()
        ip.delete_floor_assert()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_6_delete_building(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_infrastructure()
        ip = InfraPage(init_env)
        ip.delete_building()
        ip.delete_build_assert()
