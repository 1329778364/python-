#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 集合的表示与查找.py
# @Date  : 2019/4/1 0001
# @Contact : 1329778364@qq.com
# @Author: DeepMan


class SetNode:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent


class Set:
    def __init__(self):
        self.setlist = []
        self.maxsize = 10

    def build_set(self):
        for i in range(self.maxsize):
            node = SetNode(data=i + 1, parent=-1)
            self.setlist.append(node)
        self.setlist[3].parent = 0
        self.setlist[4].parent = 0
        self.setlist[5].parent = 1
        self.setlist[6].parent = 1
        self.setlist[7].parent = 2
        self.setlist[8].parent = 2
        self.setlist[9].parent = 7

    def find(self, x):
        i = 0
        while (i < self.maxsize) and self.setlist[i].data != x:
            i += 1
        if self.maxsize <= 1:
            return -1
        while self.setlist[i].parent >= 0:
            i = self.setlist[i].parent  # i 是parent 的下标哦
        return i  # 找到树根的下标 比如3 的下标是2

    def lujingyasuo_find(self, x):
        if self.setlist[x] < 0:
            return x
        else:
            self.setlist[x] = self.lujingyasuo_find(self.setlist[x])
            return self.setlist[x]

    def Union(self, x1, x2):
        root1 = self.find(x1)
        root2 = self.find(x2)
        if root1 != root2:  # 表明不是一个集合
            self.setlist[root1].parent = root2  # 将x1挂载x2上

    def Tree_Heigh_Union(self, x1, x2):  # 假设此时 已经是树根 存储的是-1
        if self.setlist[x1] < self.setlist[x2]:
            self.setlist[x2] = x1  # 矮的树归并到高的树上
        else:
            if self.setlist[x1] == self.setlist[x2]:
                self.setlist[x2] -= 1
            self.setlist[x1] = x2

    def Guimo_Union(self, x1, x2):  # 假设 是根节点 负数
        if self.setlist[x1] >= self.setlist[x2]:  # x2 规模更大
            self.setlist[x2] += self.setlist[x1]
            self.setlist[x1] = x2
        else:
            self.setlist[x1] += self.setlist[x2]
            self.setlist[x2] = x1

    def youhua_build_set(self):
        for i in range(self.maxsize):
            self.setlist.append(-1)  # 存储的是parent的下标 i代表的就是我们的data
        self.setlist[4] = 1
        self.setlist[5] = 1
        self.setlist[6] = 2
        self.setlist[7] = 2
        self.setlist[8] = 3
        self.setlist[9] = 3

    def youhua_find(self, x):
        # 这里直接返回parent
        # 一直往上找直到找到根节点的下标  这里就是数组的下标了 再往上就是-1 代表着当前这个节点就是根节点 我们要的就是他的下标
        while self.setlist[x] >= 0:
            x = self.setlist[x]
        return x

    def youhua_union(self, x1, x2):
        # 直接进行合并
        self.setlist[x1] = x2

    def Input_connection(self):
        numnode1, numnode2 = map(int, input("请输入两个节点的编号：").split(' '))
        root1 = self.lujingyasuo_find(numnode1)
        root2 = self.lujingyasuo_find(numnode2)
        if root1 != root2:
            self.Guimo_Union(root1, root2)
            print("成功连接%d 和 %d" % (root1, root2))

    def check_connection(self):
        numnode1, numnode2 = map(int, input("请输入两个需要检查节点的编号：").split(' '))
        root1 = self.lujingyasuo_find(numnode1)
        root2 = self.lujingyasuo_find(numnode2)
        if root1 == root2:
            print("yes")
        else:
            print("No")

    def check_network(self, n):
        counter = 0
        i = 0
        while i < n:
            if self.setlist[i] < 0:
                counter += 1
            i += 1
        if counter == 1:
            print("the network is connect")
        else:
            print("there has %d component" % counter)


if __name__ == '__main__':

    # 原始的 用数组存储集合元素***********************************************
    setlist = Set()
    # setlist.build_set()
    # 通过将 数字1 和数字2 进行合并 实际就是使1 的 parent指向了数字2  而数字2 的下标是1 所以数字1 的parent为下标1
    # setlist.Union(1, 2)
    # setlist.Union(2, 3)
    # print(setlist.setlist[1].parent)
    # print(setlist.find(10))

    # 优化存储结构***********************************************************
    """
    观察上面的结构体，其实值和数组下标差一，那可以直接把值 1 ~ n 映射为下标的 0 ~ n-1
    查找操作直接去找其父结点
    并操作直接把一棵树挂另一棵树上去
    """
    # setlist.youhua_build_set()
    # print(setlist.youhua_find(9))  # 找到 元素9 即下标9 中存储的是2 parent下标
    # setlist.youhua_union(1, 6)
    # setlist.youhua_union(3, 4)
    # print(setlist.youhua_find(5))
    # setlist.Input_connection()

    # 1 按秩归并优化Union **************************************************
    """
    直接进行归并union 会使得其中一棵树变得越来越高不利于后面的操作
    当多次并操作时，其中一个操作数固定，另一个操作数一直递增或一直递减时，树会退化成单链表

    主要 有以下两种方法：
    """
    # 1.1 根据树高进行归并，将矮的挂到高的树上
    """
    Tree_Heigh_Union()
    树高信息存储在根结点的数组值中（之前根结点的数组值都存的 -1，现在存 -树高）
    这样当"矮"树挂到"高"树上，树的高度不会增加，只有当两棵树一样高，高度才+1
    """
    # 1.2 根据规模进行归并 根据 树的元素个数多少进行归并
    """
    Guimo_Union()
    另一种解决办法是规模小的树挂到规模更高的树上去
    规模信息存储在根结点的数组值中（之前根结点的数组值都存的 -1，现在存 -元素个数）
    这样当小树挂到大树上，只有较少的树会高一层
    """

    # 2 路径压缩优化 Find ****************************************************
    """
    lujingyasuo_find()
    查找不可避免的越查越深，路径压缩可以把待查找结点与根结点
    之间的一系列结点的上一结点都变为根结点
    """

    # 3 题目： file_transfer()

    setlist.youhua_build_set()
    ins = 0
    while ins != "q":
        ins = input("输入要进行的操作:")
        if ins == "I":
            setlist.Input_connection()
        elif ins == "C":
            setlist.check_connection()
        elif ins == "S":
            setlist.check_network(setlist.maxsize)
