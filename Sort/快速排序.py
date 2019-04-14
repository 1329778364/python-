#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 快速排序.py
# @Date  : 2019/4/13 0013
# @Contact : 1329778364@qq.com
# @Author: DeepMan


"""
一、介绍
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

二、步骤
    递归实现
"""

# 快速排序的复杂实现*******************************************************
def swap(A, x1, x2):
    temp = A[x1]
    A[x1] = A[x2]
    A[x2] = temp


# 插入排序
def Insertion(A, left, right):
    for curindex in range(left, right + 1):  # 取出第一个值
        preindex = curindex - 1
        current = A[curindex]
        while preindex >= 0 and current < A[preindex]:
            # 与其前面的进行比较 如果前面的大于当前值 则将前面的值往后移
            A[preindex + 1] = A[preindex]
            preindex -= 1  # 指针往前挪
        A[preindex + 1] = current  # 移动之后空出一个位子，
        # 而pre 指向的是空额之前，所以要加以指向空格，同时也可以这么理解 当pre= -1时退出循环 将最小值填在0处


def Meidian3(A, left, right):
    center = int((left + right) / 2)
    if A[left] > A[center]:
        swap(A, left, center)
    if A[left] > A[right]:
        swap(A, left, right)
    if A[center] > A[right]:
        swap(A, center, right)
    # 将 center 交换到right-1 位置
    swap(A, center, right - 1)

    return A[right - 1]


cutoff = 10  # 当数据 规模比较小的时候 采用简单排序算法 插入排序算法


def QuickSort(A, left, right):
    if left >= right:
        return
    if cutoff <= right - left:  # 数据量较大下执行
        # 1.选择主元
        pivot = Meidian3(A, left, right)
        low = left
        high = right - 1
        # 2.子集划分，以pivot为分割点 将A分为两个独立子集 分别是大于和小于它的部分
        while low < high:
            low += 1
            high -= 1
            while(A[low] < pivot):  # 移动指针
                low += 1
            while(A[high] > pivot):
                high -= 1
            if low < high:
                swap(A, high, low)
            else:
                break
        swap(A, low, right - 1)
        # 3.递归调用对两边进行排序
        QuickSort(A, left, low - 1)
        QuickSort(A, low + 1, right)
    else:  # 当
        Insertion(A, left, right)

# 排序函数接口化


def Quich_sort(A, N):
    QuickSort(A, 0, N - 1)

A = [53, 2, 2621, 10, 20, 50, 30, 21, 54, 87, 95, 6, 5, 5, 6, 8, 3000, 12, 50]
Quich_sort(A, len(A))
print(A)


# 快速排序的简单实现******************************************************
def quick_sort(nums, start, end):
    if start >= end:
        return
    pivot = nums[start]  # 基准值
    low = start  # 左指针
    high = end  # 右指针
    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]

        while low < high and nums[low] < pivot:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    quick_sort(nums, start, low - 1)
    quick_sort(nums, low + 1, end)


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
