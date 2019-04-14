#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 分离链接法.py
# @Date  : 2019/4/14 0014
# @Contact : 1329778364@qq.com
# @Author: DeepMan
from enum import Enum
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
        self.next = None


# 表示Hash表
class HashTable:
    def __init__(self, maxsize=11):
        self.size = maxsize
        self.table = [HashEntry(0) for _ in range(self.size)]

    def Hash(self, key, tableSize):
        temp = key % tableSize
        return temp

    def find(self, key):
        pos = self.Hash(key, self.size)  # 初始散列位置
        p = self.table[pos].next
        while p is not None and p.data != key:
            p = p.next
        return p

    def Insert(self, key):
        p = self.find(key)
        if not p: # 没有找到 可以插入
            newentry = HashEntry(key)
            pos = self.Hash(key, self.size)
            # 将这个元素插入链表的表头
            newentry.next = self.table[pos].next
            self.table[pos].next = newentry
            return True
        else:
            return False

    def output(self):
        for i in range(self.size):
            p = self.table[i].next
            print(i, "\t",end="")
            while p:
                print("->", p.data, end="")
                p = p.next
            print()

if __name__ == '__main__':
    nums = [9,20,30,40,44,45,36,65,65,89,99,75,10,1,101,202,303]
    H = HashTable()
    for i in range(len(nums)):
        H.Insert(nums[i])
    H.output()









