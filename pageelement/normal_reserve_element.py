'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
'''
左侧导航栏
'''
#团队预订菜单
teamresv_menue = "//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='团队预订']"
#长包房预订菜单
longresv_menue = "//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='长包房预订']"

'''
普通预订
'''
#预订人
resvPerson = "//nz-input[@formcontrolname='resvPerson']/input"
#手机号码
reservphone = "//nz-input[@formcontrolname='phone']/input"
#增加房间个数的+号
addroomnumber_button = "//tbody[@class='ant-table-tbody']//span[text()='+']"
#选择房间号
select_roomnumber = "//span[@class='detailNum ng-star-inserted']"
#确定按钮
submit_button = "//div[@class='sub_2 ng-star-inserted']/button[@type='submit']"

#散客预订
#客人类型-会员
customer_type_member = "//span[text()='会员']/preceding-sibling::span"
#客人类型信息输入框
# customer_info_input = "//span[@class='ant-select-arrow']"
customer_info_input = '//nz-select/div'
# customer_info_input = "//nz-select[@formcontrolname='gusetUsername']/div/div/div"
#筛选出的信息下拉框
customer_info_drop_down = "//div[@style='overflow: auto;']/ul/li"


#单位预订
#客人类型-单位
customer_type_unit = "//span[text()='单位']/preceding-sibling::span"
#客人类型信息输入框
#下拉框
# customer_info_input = "//span[@class='ant-select-arrow']"
#输入框
input_info = "//div[@class='ant-select-selection__placeholder']"
# customer_info_input = "//nz-select[@formcontrolname='gusetUsername']"
# customer_info_input = "//nz-select[@formcontrolname='gusetUsername']/div/div/div"
#筛选出的信息下拉框
# customer_info_drop_down = "//div[@style='overflow: auto;']/ul/li"

assert_reserv_element = "//span[text()='修改订单']"


#中介预订
customer_type_agreementunit = "//span[text()='中介']/preceding-sibling::span"

'''
团队预订
'''
team_name_input = '//nz-input[@formcontrolname="teamName"]/input'


