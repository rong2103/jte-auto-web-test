'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from pagefuction.system_page import SystemPage
from pagefuction.damage_type_page import DamageTypePage
from pagefuction.home_page import HomePage
from pagefuction.damage_goods_page import DamageGoodsPage
from pageelement import damage_type_element
from pageelement import damage_goods_element
from testdatas import damage_goods_datas
import pytest

@pytest.mark.usefixture("init_env")
class TestDamageGoods:


    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_1_add_damagetype(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_damagegoods()
        dtp = DamageTypePage(init_env)
        dtp.add_damagetype(damage_goods_datas.add_type_name)
        dtp.is_element_dispear(damage_type_element.add_typename)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_2_edit_damagetype(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_damagegoods()
        dtp = DamageTypePage(init_env)
        dtp.edit_damagetype(damage_goods_datas.edit_type_name)
        dtp.is_element_dispear(damage_type_element.add_typename)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_3_delete_damagetype(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_damagegoods()
        dtp = DamageTypePage(init_env)
        dtp.delete_damagetype()
        dtp.is_element_dispear(damage_type_element.delete_type_button)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_4_add_damagegoods(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_damagegoods()
        dtp = DamageTypePage(init_env)
        dtp.click_damage_goods_menu()
        dgp = DamageGoodsPage(init_env)
        dgp.add_damagegoods(damage_goods_datas.add_goods_name,damage_goods_datas.add_goods_comprice,damage_goods_datas.add_goods_price,damage_goods_datas.add_beizhu)
        dgp.is_element_disappear(damage_goods_element.add_goodsname)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_5_edit_damagegoods(self,init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_damagegoods()
        dtp = DamageTypePage(init_env)
        dtp.click_damage_goods_menu()
        dgp = DamageGoodsPage(init_env)
        dgp.edit_damagegoods(damage_goods_datas.edit_goods_name,damage_goods_datas.edit_goods_comprice,damage_goods_datas.edit_goods_price,damage_goods_datas.edit_goods_beizhu)
        dgp.is_element_disappear(damage_goods_element.add_goodsname)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.smoke
    def test_6_delete_damagegoods(self, init_env):
        hp = HomePage(init_env)
        hp.click_system()
        sp = SystemPage(init_env)
        sp.click_damagegoods()
        dtp = DamageTypePage(init_env)
        dtp.click_damage_goods_menu()
        dgp = DamageGoodsPage(init_env)
        dgp.delete_damagegoods()
        dgp.is_element_disappear(damage_goods_element.delete_confirm_button)
        dgp.is_element_disappear(damage_goods_element.delete_goods_button)
