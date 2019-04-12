#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Heap.py
# @Date  : 2019/3/29 0029
# @Contact : 1329778364@qq.com
# @Author: DeepMan

"""
利用list 构建一个堆

"""


class Heap:
    # 调用的时候创建一个堆
    def __init__(self, size=0, maxsize=0):
        # 用于存储堆数据的数组 数组的下标就是二叉树的标号。并且里面的元素是按照下标进行有序存储上的。
        """
        这个堆用于插入建最大堆和调整法建最小堆 同时在堆中pop出元素的时候 还需要对堆进行调整
        :param size:
        :param maxsize:
        """
        self.heap_arr = [None for _ in range(maxsize + 1)]
        self.size = size
        self.capacity = maxsize
        self.maxdata = 10000
        self.heap_arr[0] = self.maxdata  # 哨兵节点 比所有的节点值都要的 不会再往前进行比较 提升程序效率

    # 判断是否满
    def isfull(self):
        return self.size == self.capacity

    # 判断是否为空
    def isempty(self):
        return not self.size

    # 插入 建最大堆
    def insertMax(self, item):

        if self.isfull():
            print("堆已经满了，无法插入！")
            return False
        self.size += 1  # 更新size，方便下次的入堆操作
        i = self.size  # 指向最后一个位置
        while self.heap_arr[int(  # 与父节点进行比较
                i / 2)] < item:  # 不断的向上与根节点进行比较 使其满足根节点大于子树中的任何一个元素
            self.heap_arr[int(i)] = self.heap_arr[int(i / 2)]
            i /= 2  # 每个节点的下标与其父节点的下标呈i/2的关系
        self.heap_arr[int(i)] = item  # 调整之后 应该放的位置
        return True

    # 调整建堆 首先将N个元素按顺序存入，然后再调整成堆
    def insertAdjustHeap(self, item):  # 按顺序存储便可
        self.size += 1
        i = self.size
        self.heap_arr[i] = item

    def minsort(self, i):  # 调整每一个小的子树为最小堆 整体 从下往上的调整 局部从上往下
        temp = self.heap_arr[i]
        parent = i
        while parent * 2 <= self.size:
            child = parent * 2
            if (child != self.size) and (
                    self.heap_arr[child] > self.heap_arr[child + 1]):
                child += 1
            if temp <= self.heap_arr[child]:
                break
            else:
                self.heap_arr[parent] = self.heap_arr[child]
            parent = child
        self.heap_arr[parent] = temp  # 上面的这个循环用于找到 temp 应该放在那里

    # 用于调整建最大堆
    def maxsort(self, i):
        temp = self.heap_arr[i]
        parent = i
        while parent * 2 <= self.size:
            child = parent * 2
            if (child != self.size) and (
                    self.heap_arr[child] < self.heap_arr[child + 1]):
                child += 1
            if temp >= self.heap_arr[child]:
                break
            else:
                self.heap_arr[parent] = self.heap_arr[child]
            parent = child
        self.heap_arr[parent] = temp  # 上面的这个循环用于找到 temp 应该放在那里

    def adjust(self):
        i = int(self.size / 2)
        while i > 0:
            self.minsort(i)  # i 是下标
            i -= 1

    # 删除 从根节点删除（优先队列 总是先调用优先级最高的任务 对应到 有序的堆栈就是最大值 也就是根节点了
    def deletMax(self):  # 删除根节点之后 将最后一个元素放到根节点，然后调整顺序使其满足根节点值大于其子树节点
        if self.isempty():
            print("堆栈为空 无法删除")
            return None
        max = self.heap_arr[1]  # 根就是最大的 就是我们要删除的 将其return出去
        temp = self.heap_arr[self.size]  # 取最后一个元素 放在 删除根节点后的位置
        self.size -= 1  # 更新最后一个元素的下标

        # 然后 我们更新使其满足顺序关系
        parent = 1
        while parent * 2 <= self.size:
            child = parent * 2
            if (child != self.size) and (  # child != size 判断是否有又儿子， 有的话选择两个中较小的作为child
                    self.heap_arr[child] < self.heap_arr[child + 1]):
                child += 1  # 找到左右子树中较大的儿子作为child
            if temp > self.heap_arr[child]:
                break
            else:
                self.heap_arr[parent] = self.heap_arr[child]
            parent = child
        self.heap_arr[parent] = temp  # 上面的这个循环用于找到 temp 应该放在那里
        return max

    def popmin(self): # 从上往下调整
        if self.isempty():
            print("堆栈为空 无法删除")
            return None
        min = self.heap_arr[1]
        temp = self.heap_arr[self.size]  # 表示最后一个元素
        self.size -= 1
        #  再进行调整 这里应该是  *从上往下进行调整*
        parent = 1

        while parent * 2 <= self.size:  # 表明有子节点
            child = parent * 2
            # 从左右子节点中找到较小者
            if (child != self.size) and (
                    self.heap_arr[child] > self.heap_arr[child + 1]):  # 表明有右子节点
                child += 1  # 柚子节点较小做为我们的child节点
            if temp <= self.heap_arr[child]:
                break
            else:
                # 将较小者放到parent 位置
                self.heap_arr[parent] = self.heap_arr[child]
            # parent 指向child 继续调整child 所在的子树
            parent = child
        self.heap_arr[parent] = temp

        return min

    # 层序遍历
    def levelorderTraversal(self):
        i = 1
        print("遍历的结果是：")
        while i < self.size + 1:  # 因为最后一个数没有加
            print(self.heap_arr[i])
            i += 1
        print()

    def popmax(self):
        if self.isempty():
            print("堆栈为空 无法删除")
            return None
        maxnum = self.heap_arr[1]  # 要弹出的元素
        temp = self.heap_arr[self.size]  # 表示最后一个元素
        self.size -= 1
        #  再进行调整 这里应该是  *从上往下进行调整*
        parent = 1

        while parent * 2 <= self.size:
            child = parent * 2
            if (child != self.size) and (
                    self.heap_arr[child] < self.heap_arr[child + 1]):
                child += 1
            if temp >= self.heap_arr[child]:
                break
            else:
                self.heap_arr[parent] = self.heap_arr[child]
            parent = child
        self.heap_arr[parent] = temp

        return maxnum

nums = [3, 2, 2621, 10, 20, 50, 30, 21, 54, 87, 95, 6, 5, 5, 6, 8, 262]


if __name__ == '__main__':

    # 插入建最大堆*****************************
    """
    1. 插入法 建最大堆

    通过插入，将 N 个元素一个一个相继插入到一个初始为空的堆中去，其时间代价最大是 O(NlogN)
    O(NlogN)（每次插入是 logN，总共 N 次）
    """
    H = Heap(maxsize=100)
    for num in nums:
        H.insertMax(num)
    H.levelorderTraversal()

    # 从堆栈中取出最大值
    for i in range(H.size):
        print(H.deletMax())  # 弹出之后还要将其调整为大顶堆

    # 调整建最小堆********************************************************
    """
    2. 调整建最小堆

    将 N 个元素直接按顺序存入，再调整各结点的位置（简单说来，对于从最后一个有孩子结点的结点来说，
    其本身结点和孩子结点共同构成"子最小堆"，借助前面删除的想法，
    对每个"子最小堆"排序，当排序完成，整个最小堆也建立成功），时间代价是 O(n) 
    """
    H2 = Heap(maxsize=100)
    for num in nums:
        H2.insertAdjustHeap(num)
    H2.adjust()
    H2.levelorderTraversal()

    print("*" * 50)
    for i in range(H2.size):  # 从最小堆中弹出元素
        print(i, H2.popmin())

    # 调整建最大堆***********************************************************
    H3 = Heap(maxsize=100)
    for num in nums:
        H3.insertAdjustHeap(num)

    # 调整堆
    i = int(H3.size / 2)
    while i > 0:
        H3.maxsort(i)  # i 是下标
        i -= 1

    print("*" * 50)
    for i in range(H3.size):  # 从最小堆中弹出元素
        print(i, H3.popmax())








