#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 平衡二叉树.py
# @Date  : 2019/3/29 0029
# @Contact : 1329778364@qq.com 
# @Author: DeepMan

"""
解决的问题：是设计怎样的树结构才能使查找的效率比较高。用Asl来进行衡量

平衡因子： 左右子树的高度差  要求 平衡因子 <=1 这样的数称为平衡儿二叉树  使得树的高度 logn

在我们将数据插入平衡二叉树的时候会导致树变得不平衡，那怎么进行调整才能够变得平衡呢：


1、右单旋  麻烦节点在发现者节点的右子树的右子树上（作为左右子节点都行），我们进行的调整称为  RR  将右子树的位置提升为根节点
2、左单旋  同理                左     左
调整的时候 只针对相距最近的发现者与破坏者
还有LR RL 旋转
同时旋转之后的相对大小 要保持
插入数据的时候 要注意更新 每个节点的 平衡因子

"""
from Tree import *

# 以下 函数都是一个模块，针对发现者 和破坏者 在一棵复杂的树中  我们就需要调用这些简单的操作 来完成数的平衡
# 其基本思路是把 B 的右子树腾出来挂到 A 的左子树上，返回 B 作为当前子树的根
def LLRotation(A): # A是被破坏节点
    B = A.left
    A.left = B.right
    B.right = A

    A.heigh = max(getHeight(A.left), getHeight(A.right)) + 1
    B.heigh = max(getHeight(B.left), A.heigh) + 1

    return B # 将B 作为根节点


# 其基本思路是把 B 的左子树腾出来挂到 A 的右子树上，返回 B 作为当前子树的根
def RRRotation(A):
    B = A.right
    A.right = B.left # 保证大小关系
    B.left = A

    A.heigh = max(getHeight(A.left), getHeight(A.right)) + 1
    B.heigh = max(getHeight(B.left), A.heigh) + 1

    return B

# 基本思想:是先将 B 作为根结点进行 LL 单旋转化为 RR 插入，
# 再将 A 作为根结点进行 RR单旋（先 LL 再 RR）
def RLRotation(A):
    A.right = LLRotation(A.right)
    return RRRotation(A)

def LRRotation(A): # 先 RR 再 LL
    A.left = RRRotation(A.left)
    return LLRotation(A)


def getHeight(A):
    if A == None:
        return -1
    else:
        return A.heigh


def Insert(x, BST):
    if not  BST:
        BST = BinaryTree(data=x)
    else:
        if x < BST.data:
            BST.left = Insert(x, BST.left)
            if (getHeight(BST.left) - getHeight(BST.right)) == 2:
                if x < BST.left.data:
                    BST = LLRotation(BST)
                elif BST.left.data < x :
                    BST= LRRotation(BST)
        elif BST.data < x :
            BST.right = Insert(x, BST.right)
            if (getHeight(BST.right) - getHeight(BST.left)) == 2:
                if x < BST.right.data:
                    BST = RLRotation(BST)
                elif BST.right.data < x:
                    BST = RRRotation(BST)
    BST.heigh = max(getHeight(BST.left), getHeight(BST.right)) + 1
    return BST


# 层序遍历
def levelorder(BST):
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


def main():
    node_list = [89, 8, 64, 64, 9, 49, 65, 146, 4, 61, 5, 46]

    # 创建一棵树
    tree = BinaryTree(10)
    for node in node_list:
        BST = Insert(node, tree)

    levelorder(BST) # 先序遍历  根 左 右

main()















