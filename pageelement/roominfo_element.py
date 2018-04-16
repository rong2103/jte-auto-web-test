'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import room_info_datas
#新增
#新增房间按钮
add_room_button = "//span[text()='新增房间']/.."
#楼层选择
add_floor_select = "//nz-select[@formcontrolname='floor']/div"
add_floor_value = "//ul[@class='ant-select-dropdown-menu ant-select-dropdown-menu-vertical ant-select-dropdown-menu-root']/li"
#房型选择
add_roomtype_select = "//nz-select[@formcontrolname='roomType']/div"
add_roomtype_value = "//ul[@class='ant-select-dropdown-menu ant-select-dropdown-menu-vertical ant-select-dropdown-menu-root']/li"

add_room_number = "//nz-input[@formcontrolname='roomNumber']/input"
add_room_innerTel = "//nz-input[@formcontrolname='innerTel']/input"
add_room_outTel = "//nz-input[@formcontrolname='outTel']/input"

add_savebutton = "//button[text()='保存']"

#修改
edit_room_button = "//td[text()='%s']/../td/span" %room_info_datas.add_roomnumber

#删除
delete_room_button = "//td[text()='%s']/../td/nz-popconfirm/span" %room_info_datas.edit_roomnumber
#删除确认按钮
delete_confirm_button = "//span[text()='确定']/.."


#批量新增
batch_add_button = "//span[text()='批量新增房间']/.."
#房间号前缀
batchadd_roomnumber_fix = "//nz-input[@formcontrolname='roomNumberPrefix']/input"
#房间号开始
batchadd_roomnumber_start = "//nz-input[@formcontrolname='roomNumberStart']/input"
#房间号结束
batchadd_roomnumber_end = "//nz-input[@formcontrolname='roomNumberEnd']/input"
#电话分机开始
batchadd_phonesub_start = "//nz-input[@formcontrolname='phoneSubStart']/input"
#电话分机结束
batchadd_phonesub_end = "//nz-input[@formcontrolname='phoneSubEnd']/input"
#电话外线开始
batchadd_phoneout_start = "//nz-input[@formcontrolname='phoneOutStart']/input"
#电话外线结束
batchadd_phoneout_end = "//nz-input[@formcontrolname='phoneOutEnd']/input"
#保存
batchadd_savebutton = "//button[text()='保存']"

#批量新增后删除房间
batchadd_delete_button = "//td[text()='%s']/../td/nz-popconfirm/span" %room_info_datas.batch_add_roomnumber_start
