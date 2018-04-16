'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import room_maintain_datas
#新增
#新增房型按钮
add_roomtype_button = "//span[text()='新增房型']/.."
#新增界面-房型字段
roomtype_name = "//nz-input[@formcontrolname='name']/input"
#新增界面-可入住数
availableNumber = '//nz-input[@formcontrolname="availableNumber"]/input'
#新增界面-押金
deposit = '//nz-input[@formcontrolname="deposit"]/input'
#新增界面-简称
alias = '//nz-input[@formcontrolname="alias"]/input'
#新增界面-门市价
price = '//nz-input[@formcontrolname="price"]/input'
#新增界面-超预订数
exceedReserveNumber = '//nz-input[@formcontrolname="exceedReserveNumber"]/input'
#备注
beizhu = "//textarea"
#新增界面-保存按钮
savebutton = "//button[text()='保存']"

#修改
#新增数据对应的修改按钮
modify_button = "//td[text()='%s']/../td/span[text()='修改']" %room_maintain_datas.roomtype_name

#禁用
disable_button = "//td[text()='%s']/../td/span/span" %room_maintain_datas.edit_roomtype_name
#启用
enable_button = "//td[text()='%s']/../td/span/span" %room_maintain_datas.edit_roomtype_name

#列表状态字段
status = "//td[text()='%s']/../td[7]" %room_maintain_datas.edit_roomtype_name
#删除
#删除修改后的房型
delete_button = "//td[text()='%s']/../td/nz-popconfirm/span" %room_maintain_datas.edit_roomtype_name
#删除确认按钮
delete_confirm_button = "//span[text()='确定']/.."
