'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import damage_goods_datas

#点击损物赔偿物品菜单
damage_goods_menu = "//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='损物赔偿物品']"

#新增损物类型
#新增按钮
add_type_button = "//span[text()='新增类型']/.."
#类型名称
add_typename = "//nz-input[@name='leakName']/input"
#确定按钮
add_savebutton = "//span[text()='确定']/.."

#编辑损物类型
#修改按钮
edit_type_button = "//td[text()='%s']/following-sibling::td/span" %damage_goods_datas.add_type_name

#删除类型
#删除按钮
delete_type_button = "//td[text()='%s']/following-sibling::td/nz-popconfirm/span" %damage_goods_datas.edit_type_name
delete_confirm_button = "//div[@class='ant-popover-inner-content']//span[text()='确定']/.."
