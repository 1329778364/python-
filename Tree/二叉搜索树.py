#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉搜索树.py
# @Date  : 2019/3/28 0028
# @Contact : 1329778364@qq.com
# @Author: DeepMan


"""
分别在左右子树中进行递归查找
当相等的时候返回
"""
from Tree import *


node_list = [89, 8, 64, 64, 9, 49, 65, 146, 4, 61, 5, 46]

# 创建一棵树
tree = BinaryTree(10)
for node in node_list:
    tree.insert(node, tree)


# 递归查找
def find(x, BST):
    if not BST:  # 如果树为空 则直接return
        return
    if x < BST.data:
        return find(x, BST.left)
    if x > BST.data:
        return find(x, BST.right)
    if x == BST.data:
        return BST
# print(find(10, tree).right.data)

# 非递归查找  对于上面这种 尾递归 可以使用循环来实现


def iterfind(x, BST):

    while(BST):
        if x < BST.data:
            BST = BST.left
        if x > BST.data:
            BST = BST.right
        if x == BST.data:
            return BST
    return None

# print(iterfind(10, tree).right.data)

# 查找最小值的递归实现**************************************************


def findmin(BST):  # 最小值在最左边
    if not BST:
        return None
    elif BST.left:
        return findmin(BST.left)
    else:
        return BST
# print(findmin(tree).data)


# 查找最大值 的 非递归实现 最大元素在最右边
def iterfindmax(BST):

    while BST.right:
        BST = BST.right
    return BST
# print(iterfindmax(tree).data)


# 插入元素的操作
def insert(valve, BST):
    """插入数据， 首先要找到对应插入的位置，再进行插入操作
    :param valve:
    :param BST:
    :return:
    """
    if not BST:
        BST = BinaryTree(valve)
    else:
        if valve < BST.data:
            BST.left = insert(valve, BST.left)
        if valve > BST.data:
            BST.right = insert(valve, BST.right)

        # 如果已经存在则什么都不做

    return BST

# print(iterfindmax(insert(256, tree)).data)


# 二叉树的删除 ***************************************************************
"""
对于要删除节点包含左右儿子节点的情况：
1：取右子树中最小的元素替代 （一定在右子树的最左边，没有左儿子）
2: 取左子树中最大的元素替代 （一定在左子树的最右边，没有右儿子）
"""


def delet(x, BST):
    if not BST:  # not None  当为None的时候进入
        print("do not find ")
    elif x < BST.data:
        BST.left = delet(x, BST.left)
    elif x > BST.data:
        BST.right = delet(x, BST.right)
    elif x == BST.data:  # 这时候就找到了
        if BST.left and BST.right:  # 如果有两个儿子节点 则利用上面的那种情况进行解决
            temp = findmin(BST.right)  # 找到右子树的最小元素进行替代
            BST.data = temp.data
            BST.right = delet(BST.data, BST.right)  # 删除那个最小的节点
        else:  # 被删除节点没有子节点 或 只有一个子节点
            if not BST.right:  # 右节点为空
                BST = BST.left
            elif not BST.left:  # 左节点为空
                BST = BST.right
    return BST


bst = delet(146, tree)
print(find(146, bst))
