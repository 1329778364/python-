#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : example.py
# @Date  : 2019/4/4 0004
# @Contact : 1329778364@qq.com
# @Author: DeepMan
import numpy as np

# 邻接矩阵 包含了四个点
A = np.matrix([
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]],
    dtype=float)

# 每个点包含的特征
x = np.matrix([
    [i, -i]
    for i in range(A.shape[0])], dtype=float)
# print(x)
# [[ 0.  0.]
#  [ 1. -1.]
#  [ 2. -2.]
#  [ 3. -3.]]

print(A*x) # 得到的是当前vertex的所有邻居节点的特征之和,
# ,换句话说，图卷积层将每个节点表示为其相邻节点的聚合 当然这里仅仅是使用了邻接矩阵
# 节点的聚合表征不包含它自己的特征！该表征是相邻节点的特征聚合，因此只有具有自环（self-loop）的节点才会在该聚合中包含自己的特征 [1]。
# [[ 1. -1.]
#  [ 5. -5.]
#  [ 1. -1.]
#  [ 2. -2.]]

## 添加自环解决自身特征无法融入问题
I = np.matrix(np.eye(A.shape[0]))

A_Hat = A + I
print(A_Hat)
# [[1. 1. 0. 0.]
#  [0. 1. 1. 1.]
#  [0. 1. 1. 0.]
#  [1. 0. 1. 1.]]




















