'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from pagefuction.system_page import SystemPage
from pagefuction.hire_type_page import HireTypePage
from pagefuction.hire_goods_page import HireGoodsPage
from pagefuction.home_page import HomePage
from pageelement import hire_type_element
from pageelement import hire_goods_element
from testdatas import hire_goods_datas
import pytest

@pytest.mark.usefixture("init_env")
class TestHireGoods:

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_1_add_hiretype(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_hiregoods()
        htp = HireTypePage(init_env)
        htp.add_hiretype(hire_goods_datas.add_type_name)
        htp.is_element_dispear(hire_type_element.add_type_name)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_2_edit_hiretype(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_hiregoods()
        htp = HireTypePage(init_env)
        htp.edit_hiretype(hire_goods_datas.edit_type_name)
        htp.is_element_dispear(hire_type_element.add_type_name)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_3_delete_hiretype(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_hiregoods()
        htp = HireTypePage(init_env)
        htp.delete_hiretype()
        htp.is_element_dispear(hire_type_element.delete_type_button)


    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_4_add_hiregoods(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_hiregoods()
        htp = HireTypePage(init_env)
        htp.click_hiregoods_menu()
        hgp = HireGoodsPage(init_env)
        hgp.add_hiregoods(hire_goods_datas.add_goods_name,hire_goods_datas.add_goods_price,hire_goods_datas.add_goods_beizhu)
        hgp.is_element_exist(hire_goods_element.edit_hiregoods_button)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_5_edit_hiregoods(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_hiregoods()
        htp = HireTypePage(init_env)
        htp.click_hiregoods_menu()
        hgp = HireGoodsPage(init_env)
        hgp.edit_hiregoods(hire_goods_datas.edit_goods_name, hire_goods_datas.edit_goods_price,
                           hire_goods_datas.edit_goods_beizhu)
        hgp.is_element_exist(hire_goods_element.delete_hiregoods_button)


    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_6_delete_hiregoods(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_hiregoods()
        htp = HireTypePage(init_env)
        htp.click_hiregoods_menu()
        hgp = HireGoodsPage(init_env)
        hgp.delete_hiregoods()
        hgp.is_element_disappear(hire_goods_element.delete_hiregoods_button)