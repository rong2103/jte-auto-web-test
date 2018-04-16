'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import virtual_roomtype_datas
#新增
#新增房型按钮
add_roomtype_button = "//span[text()=' 新增房型']/.."
#虚拟房型
virtual_roomtype_name = "//nz-input[@formcontrolname='virtualName']/input"
#实体房型下拉框
room_type_select = "//*[@name='typeCode']"
#实体房型下拉值
room_type_value = "//div[@style='overflow: auto;']//li"
#描述
beizhu = "//textarea"
#保存按钮
savebutton = "//span[text()='新增虚拟房型']/ancestor::div[@class='ant-modal-content']//button[@ng-reflect-nz-type='primary']"

#修改
edit_virtual_roomtype_button = "//td[text()='%s']/../td/span" %virtual_roomtype_datas.virtual_roomtype_name
edit_savebutton = "//span[text()='编辑虚拟房型']/ancestor::div[@class='ant-modal-content']//button[@ng-reflect-nz-type='primary']"

#删除按钮
# delete_virtual_roomtype_button = "//nz-popconfirm/span"
delete_virtual_roomtype_button = "//td[text()='%s']/../td/nz-popconfirm/span" %virtual_roomtype_datas.edit_roomtype_name
#删除确认弹框
delete_confirm_button = "//span[text()='确定']/.."

#批量删除
check_box= "//input[@type='checkbox']"
# check_box = "//td[text()='%s']//preceding-sibling::td//span/span" %virtual_roomtype_datas.batch_virtual_roomtype
batch_delete_button = "//span[text()=' 批量删除']/.."
