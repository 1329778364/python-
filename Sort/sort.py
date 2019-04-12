#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort.py
# @Date  : 2019/4/10 0010
# @Contact : 1329778364@qq.com
# @Author: DeepMan
from Tree import Heap
# import sys
# sys.setrecursionlimit(1000000)

class sortAlgrithm:
    def __init__(self):
        """
        这是一个包含了各种基本排序算法的类: 默认是升序排序 下标大的存储较大的数
        """
        self.A = [53, 2, 2621, 10, 20, 50, 30, 21,
                  54, 87, 95, 6, 5, 5, 6, 8, 3000, 12]
        self.N = len(self.A)

        self.A1 = [1, 13, 24, 26, 56, 78, 2, 15, 27, 38, 96, 1001]
        self.B = [2, 15, 27, 38, 96, 1001]
        self.C = [None for _ in range(len(self.A1) + len(self.B))]

    # 交换两个元素 传入两个下标

    def swap(self, x1, x2):
        temp = self.A[x1]
        self.A[x1] = self.A[x2]
        self.A[x2] = temp

    # 冒泡排序
    def Bubble(self):
        for i in range(self.N, 0, -1):
            for j in range(i - 1):
                if self.A[j] > self.A[j + 1]:
                    self.swap(j, j + 1)

    # 插入排序
    def Insertion(self):
        for curindex in range(1, self.N):  # 取出第一个值
            preindex = curindex - 1
            current = self.A[curindex]
            while preindex >= 0 and current < self.A[preindex]:
                # 与其前面的进行比较 如果前面的大于当前值 则将前面的值往后移
                self.A[preindex + 1] = self.A[preindex]
                preindex -= 1  # 指针往前挪
            self.A[preindex + 1] = current  # 移动之后空出一个位子，
            # 而pre 指向的是空额之前，所以要加以指向空格，同时也可以这么理解 当pre= -1时退出循环 将最小值填在0处

    # 希尔排序
    def ShellSort(self):
        D = int(self.N / 2)
        while D > 0:  # 调整排序的间隔
            for curindex in range(D, self.N, D):  # 里面就是插入排序（改变在于排序的间隔由原来的1变为D）
                                                  # 实验发现1的时候也是可以的
                preindex = curindex - D
                current = self.A[curindex]
                while preindex >= 0 and current < self.A[preindex]:
                    self.A[preindex + D] = self.A[preindex]
                    preindex -= D
                self.A[preindex + D] = current
            D /= 2
            D = int(D)

    def SedgewickShell(self):
        # 关键在D值的选取方式
        # 生成 D
        d1 = [9 * 4**i - 9 * 2**i + 1 for i in range(0, 10)]
        d2 = [4**(i) - 3 * 2**(i) + 1 for i in range(2, 10)]
        DD = []
        for i in range(len(d1)):
            DD.append(d1[i])
            if i < len(d2):
                DD.append(d2[i])
        # print(DD[1::-1])

        for D in DD[1::-1]:
            for curindex in range(D, self.N, D):  # 里面就是插入排序（改变在于排序的间隔由原来的1变为D）
                print(curindex)
                # 实验发现1的时候也是可以的
                preindex = curindex - D
                current = self.A[curindex]
                while preindex >= 0 and current < self.A[preindex]:
                    self.A[preindex + D] = self.A[preindex]
                    preindex -= D
                self.A[preindex + D] = current

    # 选择排序
    def SelectSort(self):
        lastindex = len(self.A) - 1
        # 利用最大堆进行调整来实现 这种方法最好
        for i in range(int((lastindex - 1) / 2), -1, -1):  # 从下往上
            # 得到最大堆 len(self.A)-1 表示最后一个元素的下标
            self.PercDown(i, lastindex)

        # 然后 根节点 元素 与堆的最后一个元素调换，并屏蔽最后一个元素，重新得到最大堆
        # 最后 得到一个完全有序的数组
        for i in range(lastindex, -1, -1):
            self.swap(0, i)
            self.PercDown(0, i - 1)

        # 利用最小堆来实现 N*log(N) *********************************************
        # 创建一个最小堆
        #
        # minH = Heap(maxsize=100)
        # for num in self.A:
        #     minH.insertAdjustHeap(num)
        # minH.adjust()
        #
        # temp = [0 for i in range(len(self.A))]  # 缺点1 是需要额外的空间
        # for i in range(self.N):
        #     temp[i] = minH.popmin()
        # for i in range(self.N):
        #     self.A[i] = temp[i]  # 2 是 复制也是需要时间的

        # 简单实现**************************************************************
        # for i in range(self.N):
        #     minPosition = 0
        #     if i < self.N:
        #         temp = self.A[i:self.N]
        #         minPosition = temp.index(min(temp)) + i # 这里直接使用min 来查找最小值的下标
        #     self.swap(i, minPosition)

    def PercDown(self, i, lastindex):  # 从上往下进行调整
        parent = i  # int((len(self.A)-1)/2) # 指向最后一个 有子节点的元素， 然后从后往前进行调整
        temp = self.A[parent]

        while 2 * parent + 1 <= lastindex:  # 从上往下
            child = parent * 2 + 1
            # 计算len 的时候包括了下标为0 的元素  所以len -1 才表示最后一个元素的index
            # 相等的时候表示到达最后一个元素
            if child != lastindex and self.A[child] < self.A[child + 1]:
                child += 1
            if temp < self.A[child]:
                self.A[parent] = self.A[child]
            else:
                break
            parent = child  # 最后 parent 指向了chilid需要对其进行赋值
        self.A[parent] = temp

    # 归并排序 (合并两个有序子列)
    def Merge_simplify(self, A, B, C):

        # 简单实现： # 三个指针分别指向三个数组的下标 *********************************************
        # 不断移动判断大小然后存储到第三方数组，当有一个数组走到最后下标，将另一个数组拷贝到C数组
        i, j, k = 0, 0, 0
        for k in range(len(C)):
            if i < len(A) and j < len(B):
                if A[i] < B[j]:  # A < B 取A
                    C[k] = A[i]
                    i += 1
                else:
                    C[k] = B[j]
                    j += 1
            else:  # 表明 有一个已经到达末尾
                if i < len(A):
                    C[k] = A[i]
                    i += 1
                elif j < len(B):
                    C[k] = B[j]
                    j += 1
        print(C)

    # 针对的是两个 有序数列 进行归并
    def Merge(self, A, tempA, L, R, RightEnd):  # L, R 左右起点 ，RightEnd 右终点
        leftEnd = int(R - 1)  # 左边子列终点 假设两个子列是挨着的
        temp = int(L)  # 存放结果数组的初始位置
        numElements = int(RightEnd - L + 1)
        while (L <= leftEnd and R <= RightEnd):
            if (A[int(L)] <= A[int(R)]):
                tempA[int(temp)] = A[int(L)]
                temp += 1
                L += 1
            else:
                tempA[int(temp)] = A[int(R)]
                temp += 1
                R += 1
        # 表示其中一个 序列为空了 下面进行直接复制
        while (L <= leftEnd):
            tempA[int(temp)] = A[int(L)]
            temp += 1
            L += 1
        while (R <= RightEnd):
            tempA[temp] = A[int(R)]
            temp += 1
            R += 1

        # 巧妙之处
        for i in range(numElements):
            A[int(RightEnd)] = tempA[int(RightEnd)]
            RightEnd -= 1

    # 利用分治思想将序列进行分解然后进行归并排序， 递归的对子序列进行排序， 然后进行归并两个子序列
    def Msort(self, A, tempA, L, RightEnd):
        if L < RightEnd:
            center = int((L + RightEnd) / 2) # 不取整的话容易导致无限循环好多次
            self.Msort(A, tempA, L, center)
            self.Msort(A, tempA, center + 1, RightEnd)
            self.Merge(A, tempA, L, center + 1, RightEnd)

    # 将上面的函数进行接口化
    def MergeSort(self, A, N):
        tempA = [0 for _ in range(N)]
        if tempA is not None:
            self.Msort(A, tempA, 0, N-1)
            tempA = None
        else:
            print("no memery")


s = sortAlgrithm()
s1 = sortAlgrithm()

# # 冒泡排序*****************************
# s.Bubble()
#
# # 希尔排序 ****************************
# s.ShellSort()
# print(s.A)
#
# s1.SedgewickShell()
# print(s1.A)
#
# # 插入排序 ****************************
# s1.Insertion()
# print(s1.A)

# 选择排序* *****************************
s2 = sortAlgrithm()
# s2.SelectSort()
# print(s2.A)

# 归并排序**************************************************
# *********************************************************

# 针对的是两个分段有序数列的 归并
tempA = [0 for _ in range(len(s2.A))]
s2.Merge(s2.A1, tempA, 0, 6, len(s2.A1) - 1)
print(s2.A1)

# 递归算法，分治思想将序列进行排序（利用归并排序作为元算法）
# 针对无序数组 非常重要的思想
s3 = sortAlgrithm()
s3.MergeSort(s3.A, s3.N)
print(s3.A)

# 非递归算法


def fuck():
    print("jbiobva")

# aeibfvobvoiab vlav
# sklnbak

# wlaw

