#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 归并排序非递归.py
# @Date  : 2019/4/13 0013
# @Contact : 1329778364@qq.com
# @Author: DeepMan

"""
归并排序在外排的时候使非常有用的，在内排的时候不用，来回进行拷贝

"""
def Merge1(A, tempA, L, R, RightEnd):  # L, R 左右起点 ，RightEnd 右终点
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


def Merge_pass(A, tempA, N, length):
    # 先将前面的偶数对进行归并
    k = 0
    for i in range(0, N - 2 * length + 1, 2 * length):
        Merge1(A, tempA, i, i + length, i + 2 * length - 1)
        k = i
    if k + length < N:  # 归并最后 两个子列
        Merge1(A, tempA, k, k + length, N - 1)
    else:            # 只有一个子列 直接进行=拷贝即可
        for j in range(k, N):
            tempA[j] = A[j]


def merge_sort(A, N): # 稳定的
    length = 1  # 子序列长度
    tempA = [0 for _ in range(N)]
    if tempA != None:
        while(length<N):
            Merge_pass(A, tempA,N, length)
            length *= 2
            Merge_pass(tempA, A , N, length)
            length *= 2
    else:
        print("no memery")

A = [53, 2, 2621, 10, 20, 50, 30, 21,
                  54, 87, 95, 6, 5, 5, 6, 8, 3000, 12]


merge_sort(A, len(A))
print(A)
