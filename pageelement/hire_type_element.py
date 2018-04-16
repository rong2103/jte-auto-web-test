'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import hire_goods_datas
hire_goods_menu = "//ul[@class='ant-menu ant-menu-root ant-menu-dark ant-menu-inline']//a[text()='租借物品']"

#新增类型按钮
add_type_button = "//span[text()='新增类型']/.."
add_type_name = "//nz-input/input"
#确定按钮
add_savebutton = "//span[text()='确定']/.."

#修改类型
edit_type_button = "//td[text()='%s']/../td/span" %hire_goods_datas.add_type_name

#删除
delete_type_button = "//td[text()='%s']/../td/nz-popconfirm/span" %hire_goods_datas.edit_type_name
delete_confirm_button = "//div[@class='ant-popover-inner-content']//span[text()='确定']/.."