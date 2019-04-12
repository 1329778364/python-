#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p64_path_of_stack.py
# @Date  : 2019/3/31 0031
# @Contact : 1329778364@qq.com
# @Author: DeepMan


"""
https://www.bilibili.com/video/av18586085/?p=64
题目
将一系列给定数字插入一个初始为空的小顶堆H[]。随后对任意给定的下标i，打印从H[i]到根结点的路径。
输入格式:
每组测试第1行包含2个正整数N和M(≤1000)，分别是插入元素的个数、以及需要打印的路径条数。下一行给出区间[-10000, 10000]内的N个要被插入一个初始为空的小顶堆的整数。最后一行给出M个下标。
输出格式:
对输入中给出的每个下标i，在一行中输出从H[i]到根结点的路径上的数据。数字间以1个空格分隔，行末不得有多余空格。

输入样例:

    5 3
    46 23 26 24 10
    5 4 3

输出样例:

    24 23 10
    46 23 10
    26 10
"""
from Tree.Heap import *

__all__ = ["minHeap"]

class minHeap(Heap):
    def __init__(self,size=0, maxsize=1005):
        super(minHeap, self).__init__(size=size, maxsize=maxsize)
        self.mindata = -100000
        self.heap_arr[0] = self.mindata  # 哨兵值

    def insert(self, item):
        self.size += 1
        i = self.size
        while self.heap_arr[int(i / 2)] > item:
            self.heap_arr[int(i)] = self.heap_arr[int(i / 2)]
            i /= 2
        self.heap_arr[int(i)] = item

    def printPath(self, i):
        while i >= 1:

            print(self.heap_arr[int(i)])
            if i != 1:
                print("^")
            i /= 2
        print()


if __name__ == '__main__':
    minheap = minHeap()

    # 建堆
    for num in nums:
        minheap.insert(num)

    # 遍历
    minheap.levelorderTraversal()

    # 输入我们要查找的
    minheap.printPath(8) # 表示我们要查找的元素的下标。
