'''
基础设施模块的元素定位文件
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-

from testdatas import infra_datas
#左侧导航栏元素
room_maintain_menu = "//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='房型维护']"
room_info_menu = "//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='房间信息']"
virtual_roomtype_menu = "//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='虚拟房型']"
roomlock_maintain_menu = "//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='门锁维护']"

# 新增楼栋按钮
addbuilding_button = "//span[text() = '新增楼栋'] /.."
# 新增楼层按钮
addfloor_button = "xpath=//span[text()='新增楼层']/.."
# 楼栋名称输入框
buildingname_input = "//nz-input[@name='buildingName']/input"
# 新增楼栋备注输入框
remark_input = "//nz-input[@name='remark']/textarea"
# 新增保存按钮
# savebuilding_button = "//button[contains(text(),'保存')]"
savebuilding_button = "//span[text()='新增楼栋信息']/ancestor::div[@class='ant-modal-content']//button[@ng-reflect-nz-type='primary']"
# 已存在的楼栋列表
# building_group = "//nz-radio-group//span[2]"
# building_group = "//span[contains(text(),'%s')] %build_name"
new_building_group = "//nz-radio-group//span[contains(text(),'%s')]" % infra_datas.new_building_name

# 楼栋-修改按钮
build_edit_button = "//span[text()='修改']"
#修改-楼栋名
edit_build_name = "//nz-input[@name='buildingName']/input"
#修改楼栋备注
edit_build_remark = "//nz-input[@name='remark']/textarea"
#修改-保存按钮
edit_build_savebutton = "//span[text()='编辑楼栋信息']/ancestor::div[@class='ant-modal-content']//button[@class='ant-btn ant-btn-primary ant-btn-lg']"
edit_building_group = "//span[contains(text(),'%s')]" % infra_datas.edit_building_name

#新增楼层按钮
add_floor_button = "//span[text()='新增楼层']/.."
#开始楼层输入框
addfloor_startfloor_input = "//span[text()='新增楼层信息']/ancestor::div[@class='ant-modal-content']//nz-input-number[@name='floorstart']//input"
#结束楼层输入框
addfloor_endfloor_input = "//span[text()='新增楼层信息']/ancestor::div[@class='ant-modal-content']//nz-input-number[@name='floorEnd']//input"
#新增楼层备注输入框
addfloor_remark = "//span[text()='新增楼层信息']/ancestor::div[@class='ant-modal-content']//textarea"
#新增楼层保存按钮
addfloor_savebutton = "//span[text()='新增楼层信息']/ancestor::div[@class='ant-modal-content']//button[@class='ant-btn ant-btn-primary ant-btn-lg']"
#楼层列表中新增的楼层对象
newfloor_inlist = "//li[contains(text(),'%s')]" % infra_datas.add_startfloor

#楼层修改按钮
floor_edit_button = "//span[@class='room']/span"
#楼层
edit_floor_input = "//span[text()='修改楼层信息']/ancestor::div[@class='ant-modal-content']//input"
edit_floor_remark = "//span[text()='修改楼层信息']/ancestor::div[@class='ant-modal-content']//textarea"
edit_floor_savebutton = "//span[text()='修改楼层信息']/ancestor::div[@class='ant-modal-content']//button[@class='ant-btn ant-btn-primary ant-btn-lg']"
editfloor_inlist = "//li[contains(text(),'%s')]" % infra_datas.edit_floor

#删除楼层-删除按钮
floor_delete_button = "//span[@class='room']/nz-popconfirm/span"
floor_delete_confirm_button = "//span[text()='确定']/.."

#楼栋删除按钮
build_delete_button = "//span[@class='datail']/nz-popconfirm/span"
build_delete_confirm_button = "//span[text()='确定']/.."
