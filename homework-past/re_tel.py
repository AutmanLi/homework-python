#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: autmanli
@license: Apache Licence 
@file: re_tel.py
@time: 2018/10/12 14:59
"""

import re

class re_telandEmail(object):


    @classmethod
    def re_tel(self,tel):
        '''
        +86表示是中国电话区号,可加可不加。
        除了区号前三位可以是13[0-9]、145、147、166、173、176、177、18[0-9]
        最后8位任意
        :param email: 输入的电话号码
        :return: 匹配结果
        '''
        m= re.match(r'^(\+86-)?((13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8})$',tel)
        if m:
            print("匹配成功！")
        else:
            print("不是正确的中国手机号码")

    @classmethod
    def re_email(self,email,isZhuliu):
        '''
        主流邮箱:qq、gmail、hotmail、126、163、vip
        前面是19位字符，@后是邮箱前缀，.后是一级域名
        :param email: 输入的邮箱地址
        :param isZhuliu: 是否是主流邮箱
        :return: 匹配结果
        ^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$该表达式匹配各种邮箱
        '''
        if isZhuliu:
            m = re.match(r'[0-9a-zA-Z]{0,19}@(qq|gmail|hotmail|126|163|vip)\.[com,cn,net]{1,3}$',email)
        else:
            m = re.match(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email)

        if m:
            print("匹配成功！")
        else:
            print("不是正确的邮箱形式")


re_telandEmail.re_tel('13598546464')
re_telandEmail.re_tel('+86-18720994197')
re_telandEmail.re_tel('11298546464')
re_telandEmail.re_tel('1rewge')
print('\n')
re_telandEmail.re_email('187813@qq.com',True)
re_telandEmail.re_email('gerrwge@gmail.com',True)
re_telandEmail.re_email('ergerwg',False)
re_telandEmail.re_email('ergerwg@',False)
re_telandEmail.re_email('ergerwg@189.com',False)
