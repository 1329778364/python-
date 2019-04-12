#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二叉树的遍历.py
# @Date  : 2019/3/27 0027
# @Contact : 1329778364@qq.com
# @Author: DeepMan

# 由于我们使用非递归遍历的时候会用到堆栈 我们先定义堆栈
from Tree import *


class BinaryTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # 构建一棵树  由于递归调用需要两个参数  所以 我们可以定义连个方法  来分别对左右子树进行判定
    # 递归调用创建一棵树
    def insert(self, value, BST):
        if not BST:
            BST = BinaryTree(value)
        elif value < BST.data:  # 保证在左子树的值都小于根节点
            BST.left = self.insert(value, BST.left)
        elif value > BST.data:  # 保证在右子树的值都大于根节点
            BST.right = self.insert(value, BST.right)
        else:  # 如果相等则什么都不做
            pass
        return BST

    # 树的先序遍历***************************************************

    def preorderTraversal(self, BST):
        if BST:
            print(BST.data)
            self.preorderTraversal(BST.left)
            self.preorderTraversal(BST.right)

    # 非递归实现
    def preorder(self, BST):
        t = BST
        stack1 = stack()
        while (t or not stack1.empty()):
            while t:
                stack1.push(t)
                print(t.data)
                t = t.left
            if not stack1.empty():
                t = stack1.pop()
                t = t.right

    # 中序遍历****************************************************

    def inorderTraversal(self, BST):
        if BST:
            self.inorderTraversal(BST.left)
            print(BST.data)
            self.inorderTraversal(BST.right)

    # 中序遍历的非递归实现 （利用堆栈实现） 挽回走的时候 抛出元素
    def inorder(self, BST):
        t = BST
        stack1 = stack()
        while(t or not stack1.empty()):
            while t:
                stack1.push(t)
                t = t.left
            if not stack1.empty():
                t = stack1.pop()
                print(t.data)
                t = t.right

    # 后序遍历***************************************************

    def PostOrderTraversal(self, BST):
        if BST:
            self.PostOrderTraversal(BST.left)
            self.PostOrderTraversal(BST.right)
            print(BST.data)

    # 后序 非递归实现
    def Postorder(self, BST):
        t = BST
        s = stack()
        l = []
        s.push(t)
        while not s.empty():
            t = s.pop()
            l.append(t)
            if t.left:
                s.push(t.left)
            if t.right:
                s.push(t.right)
        l = reversed(l)
        for i in l:
            print(i.data)

    # 层序遍历
    def levelorder(self, BST):
        q = queue()
        t = BST
        if not BST:
            return
        q.append(t)
        while not q.empty():
            t = q.pop()
            print(t.data)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)


node_list = [89, 8, 64, 64, 9, 49, 65, 146, 4, 61, 5, 46]

# 创建一棵树
tree = BinaryTree(10)
for node in node_list:
    tree.insert(node, tree)


# 中序遍历
tree.inorderTraversal(tree)  # 左根右
print("*" * 50)
tree.inorder(tree)
print("*" * 20)


# 先序遍历  根 左 右
tree.preorderTraversal(tree)
print("*" * 50)
# 先序非递归
tree.preorder(tree)


# 后序遍历  左 右 根
print("*" * 50)
tree.PostOrderTraversal(tree)
# 后序 非递归
print("*" * 50)
tree.Postorder(tree)

"""
以上三种遍历方法总结

先序、中序和后序遍历过程：遍历过程中经过结点的路线一样，只是访问各结点的时机不同，即：

    先序遍历是第一次"遇到"该结点时访问
    中序遍历是第二次"遇到"该结点（此时该结点从左子树返回）时访问
    后序遍历是第三次"遇到"该结点（此时该结点从右子树返回）时访问

"""


# 层序遍历****************************************************************
"""
遍历过程：从上至下，从左至右访问所有结点

队列实现过程：

    0 根结点入队
    1 从队列中取出一个元素
    2 访问该元素所指结点
    3 若该元素所指结点的左孩子结点非空，左孩子结点入队
    4 若该元素所指结点的右孩子结点非空，右孩子结点入队
    5 循环 1 - 4，直到队列中为空
"""
print("*" * 20)
tree.levelorder(tree)


# 例子 ********************************************************

# 1. 输出叶子结点 ： 前序遍历加个没有孩子结点的约束即可

def findleaves(BTS):
    if BTS:
        if not BTS.left and not BTS.right:  # 如果没有左右节点
            print(BTS.data)
        findleaves(BTS.left)
        findleaves(BTS.right)


print("*" * 50)
findleaves(tree)

# 2  树的高度: 当前树的高度为其子树最大高度 +1


def treeheight(BST):
    hl, hr, maxh = 0, 0, 0
    if BST:
        hl = treeheight(BST.left)
        hr = treeheight(BST.right)
        maxh = max(hl, hr)
        return maxh + 1
    else:
        return 0


print(treeheight(tree))  # 5


# 3. 由两种遍历序列确定二叉树  同构
"""
前提：有一种序列必须是中序！

方法：

    根据先序（或后序）遍历序列第一个（或最后一个）结点确定根结点
    根据根结点在中序序列中分割出左右两个子序列
    对左子树和右子树分别递归使用同样的方法继续分解

例如：

前序：ABCDEFG
中序：CBDAFEG

先序遍历为"根左右"，则 A 是根，对应可以划分出中序中：(CBD)A(FEG)，CBD 为左子树，FEG 为右子树，再根据前序的 BCD，B 为根，划分出中序中 (C(B)D)A(FEG)，则 C D 分别是 B 的左右子树…最后可得树为：

                 A
                /\
               B  E
              /\  /\
             C D  F G

"""
