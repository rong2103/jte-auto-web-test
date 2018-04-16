'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
import pytest
from pagefuction.home_page import HomePage
from pagefuction.normal_reserv_page import NormalReserv
from pagefuction.reserv_detail_page import ReservDetailPage
from testdatas import reserv_datas
from pageelement import normal_reserve_element
import time

@pytest.mark.usefixture("init_env")
class TestNormalReserv:

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.smoke
    def test_1_individual_normal_reserv(self,init_env):
        hp = HomePage(init_env)
        hp.click_reserv()
        nrp = NormalReserv(init_env)
        nrp.individual_normal_reserv(reserv_datas.normal_reserv_individual_personname,reserv_datas.normal_reserv_individual_phone)
        nrp.is_exist_ele(normal_reserve_element.assert_reserv_element)
        # rdp = ReservDetailPage(init_env)
        # rdp.cancel_reserv()

    # # @pytest.mark.test
    # def test_2_member_normala_reserv(self,init_env):
    #     hp = HomePage(init_env)
    #     hp.click_reserv()
    #     nrp = NormalReserv(init_env)
    #     nrp.member_normal_reserv(reserv_datas.normal_reserv_membername)
    #     nrp.assert_ifto_orderdetail()

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.smoke
    #输入单位信息无法输入，需要调试
    def test_3_unit_normal_reserv(self, init_env):
        hp = HomePage(init_env)
        hp.click_reserv()
        nrp = NormalReserv(init_env)
        nrp.not_individual_normal_reserv(normal_reserve_element.customer_type_unit)
        time.sleep(10)
        nrp.is_exist_ele(normal_reserve_element.assert_reserv_element)

    # @pytest.mark.test
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.smoke
    def test_4_aggr_normal_reserv(self, init_env):
        hp = HomePage(init_env)
        hp.click_reserv()
        nrp = NormalReserv(init_env)
        nrp.not_individual_normal_reserv(normal_reserve_element.customer_type_agreementunit)
        time.sleep(10)
        nrp.is_exist_ele(normal_reserve_element.assert_reserv_element)