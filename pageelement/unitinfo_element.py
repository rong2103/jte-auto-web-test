'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
from testdatas import unitinfo_datas
#新增按钮
add_button = '//*[text()=" 新增"]/..'
#单位名称
new_name = '//nz-input[@name="agreementUnitName"]/input'
#联系人
new_contact_person = '//nz-input[@name="linkman"]/input'
#手机
new_phone = '//nz-input[@name="mobile"]/input'
#价格策略
new_price_strage_select = '//nz-select[@name="priceStrategyCode"]/div'
new_price_strage_value = '//div[@style="overflow: auto;"]/ul/li'
#计费规则
new_charging_rule_select = '//nz-select[@name="chargingRuleCode"]/div'
new_charging_rule_value = '//div[@style="overflow: auto;"]/ul/li'
#保存按钮
saveButton = "//span[text()='保存']/.."


#详情界面
detail_button = "//td[contains(text(),%s)]/..//span[text()='详情']" %unitinfo_datas.new_unit_name
view_toprow = "//span[text()=' > 单位详情']"
view_unitname = "//span[text()='%s']" %unitinfo_datas.new_unit_name

#修改界面
modify_button = "//td[contains(text(),%s)]/..//span[text()='修改']" %unitinfo_datas.new_unit_name
#挂账额度
debitAmount = '//nz-input-number[@name="debitAmount"]//input'
#早餐券数
couponNumber = '//nz-input[@name="couponNumber"]//input'
#银行账号
bankAccount = '//nz-input[@name="bankAccount"]/input'
#税号
dutyParagraph = '//nz-input[@name="dutyParagraph"]/input'
#电话
telephone = '//nz-input[@name="telephone"]/input'
#合同号
agreementNo = '//nz-input[@name="agreementNo"]/input'
#邮箱
email = '//nz-input[@name="email"]/input'
#地址
address = '//nz-input[@name="address"]/input'
#备注
remark = '//textarea[@name="remark"]'


#禁用
more_button = "//td[contains(text(),%s)]/..//span/nz-dropdown" %unitinfo_datas.edit_unitname
disable_button = '//div[@class="cdk-overlay-container"]/div/div/div/ul/li/a'
status = "//td[contains(text(),%s)]/../td[9]" %unitinfo_datas.edit_unitname
