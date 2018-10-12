#!/usr/bin/env python
# encoding: utf-8

import inspect
"""
@version: ??
@author: autmanli
@license: Apache Licence 
@file: class_learn.py
@time: 2018/10/12 10:04
"""

class A(object):
    def eat(self):
        pass


class B(A):
    pass

class C(B):
    pass

class D(B):
    pass

class E(C,D):
    pass


print(inspect.getmro(E))
