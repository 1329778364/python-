#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符关键字散列.py
# @Date  : 2019/4/14 0014
# @Contact : 1329778364@qq.com 
# @Author: DeepMan

strs = "wlq "

"""
3. 移位法
例子（移位法）
h(“abcde”) = 'a’x32**4 + 'b’x32**3 +'c’x32**2 + 'd’x32 + ‘e’=
((('a’x32+‘b’)x32+‘c’)x32+‘d’)x32+‘e’
"""

def Hash(key, tableSize):
    h = 0
    i = 0
    while key[i] != " ":
        h = (h<<5) + ord(key[i])
        i += 1
    print(h)
    return h%tableSize

print(Hash(strs, 12))
