#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 平方探测法实现.py
# @Date  : 2019/4/14 0014
# @Contact : 1329778364@qq.com
# @Author: DeepMan


from math import *
from enum import Enum
"""

如果散列表长度是某个 4k+3（k是正整数）形式的素数时，
平方探测法就可以探查到整个散列表空间
"""
maxtablesise = 100

# 表示 一个节点的状态 有三种情况
class EntryType(Enum):
    Legitmate = 0,
    Empty = 1
    Delete = 2

# hash表中的一个单元
class HashEntry:
    def __init__(self, data):
        self.data = data
        self.info = EntryType.Empty

# 表示Hash表
class HashTable:
    def __init__(self, maxsize=10):
        self.size = maxsize
        self.table = [HashEntry(0) for _ in range(self.size)]


def nextPrime(N):  # 从N开始进行查找 一个素数
    p = N + 1 if N % 2 == 0 else N + 2
    i = 0
    while p <= maxtablesise:
        for i in range(int(sqrt(p)), 2, -1):
            if p % i == 0:
                break
        if i == 2:
            break
        p += 2
    return p

# 创建哈希表


def CreatTable(tablesize):
    size = nextPrime(tablesize)
    H = HashTable(size)
    return H


def Insert(H, key, i):
    pos = Find(H, key)
    # 如果单元格状态不是存在合法元素
    if H.table[pos].info != EntryType.Legitmate:
        H.table[pos].info = EntryType.Legitmate
        H.table[pos].data = key
    return True


def Hash(key, tableSize):
    temp = key % tableSize
    return temp

# 平方探测查找


def Find(H, key):
    Cnum = 0
    currpos = Hash(key, H.size)
    newpos = currpos
    #  如果当前单元状态不为空，且数值不等，则一直做
    while H.table[newpos].info != EntryType.Empty and H.table[newpos].data != key:
        Cnum += 1
        if Cnum % 2:
            newpos = int(currpos + (Cnum + 1) / 2 * (Cnum + 1) / 2)
            while H.size <= newpos:
                newpos -= H.size
        else:
            newpos = int(currpos - Cnum / 2 * Cnum / 2)
            while newpos < 0:
                newpos += H.size
    return newpos


def output(H):
    for i in range(H.size):
        print(i, " ", H.table[i].data)

# print(CreatTable(100).size)
if __name__ == '__main__':
    H = CreatTable(1)
    # N = int(input("请输入N："))
    num = [101, 202, 303, 404, 505,909,1010,2020]
    for i in range(len(num)):
        temp = num[i]
        Insert(H, temp, i)
    output(H)
