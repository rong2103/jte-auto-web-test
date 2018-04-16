'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import damage_goods_datas

#新增损物物品
#新增按钮
add_goods_button = "//span[text()='新增赔偿物品']/.."
#物品类型
add_goods_type_select = "//nz-select[@name='leakCode']"
add_goods_type_value = "//div[@style='overflow: auto;']/ul/li"
#物品名称
add_goodsname = "//nz-input[@formcontrolname='productName']/input"
#赔偿单价
add_goods_compPrice = "//nz-input-number[@formcontrolname='compPrice']//input"
#成本价格
add_goods_price = "//nz-input-number[@formcontrolname='price']//input"
#备注
add_goods_beizhu = "//textarea"
#确定按钮
add_goods_savebutton = "//div[@class='ng-star-inserted']/button"

#编辑损物物品
#修改按钮
edit_goods_button = "//td[text()='%s']/../td/span" %damage_goods_datas.add_goods_name

#删除类型
#删除按钮
delete_goods_button = "//td[text()='%s']/../td/nz-popconfirm/span" %damage_goods_datas.edit_goods_name
delete_confirm_button = "//div[@class='ant-popover-inner-content']//span[text()='确定']/.."
