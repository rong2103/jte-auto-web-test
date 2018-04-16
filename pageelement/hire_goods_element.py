'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import hire_goods_datas

#新增物品
add_goods_button = "//span[text()='新增租借物品']/.."
#物品类型
add_goods_select = "//form//nz-select/div/div/div"
add_goods_value = "//div[@style='overflow: auto;']/ul/li"
#物品名称
add_goodsname = "//nz-input[@formcontrolname='productName']/input"
#租借单价
add_goods_compPrice = "//nz-input-number[@formcontrolname='compPrice']//input"
#备注
add_goods_beizhu = "//textarea"
#确定按钮
add_goods_savebutton = "//div[@class='ng-star-inserted']/button"


#修改物品
edit_hiregoods_button = "//td[text()='%s']/../td/span" %hire_goods_datas.add_goods_name



#删除物品
delete_hiregoods_button = "//td[text()='%s']/../td/nz-popconfirm/span" %hire_goods_datas.edit_goods_name
delete_confirm_button = "//div[@class='ant-popover-inner-content']//span[text()='确定']/.."