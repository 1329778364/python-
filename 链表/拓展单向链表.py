#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 拓展单向链表.py
# @Date  : 2019/3/26 0026
# @Contact : 1329778364@qq.com 
# @Author: DeepMan

"""
这一节主要介绍链表的其他操作 包括交叉 环形判断。等

"""
class Node:
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None

head = Node()
# 1 2 3 4 5 6 7 8 9 顺序输入
# 9->8->7->6->5->4->3->2->1->None 这就是头插法

for i in range(1, 10):
    s = Node(i)
    temp = head.next
    head.next = s
    s.next = temp

# cur = head.next

# while cur.next != None:
#     print(cur.data,end='->')
#     cur = cur.next


"""
链表逆序**********************************************************************
"""
# 那怎么实现上述链表
#      head->9->8->7->6->5->4->3->2->1->None 的逆序呢
# 变为        None<-9<-8<-7<-6<-5<-4<-3<-2<-1

# print()
# print("后面是进行逆序")
# NewList = Node()
#
# cur = head.next

# 同样可以使用头插入的方法
# while cur is not None:
#     newnode = Node(cur.data) # 创建新节点用于接收读取到的数据
#
#     newnode.next = NewList.next
#     NewList.next = newnode
#
#     cur = cur.next # 移动指针将所有数据遍历出来


# cur = NewList.next
# while cur != None:
#     print(cur.data, end="->")
#     cur = cur.next

# 最终结果：
# 9->8->7->6->5->4->3->2->
# 后面是进行逆序
# 1->2->3->4->5->6->7->8->9->


class ListNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


def build_l(nums):
    head = ListNode(nums[0]) # 头节点
    cur = head # 移动节点
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next  # 指向 到 下一个节点
    return head  # 只要有了head 就可以将链表找到

def build_recurrent_list(nums): # 单向循环链表
    head = ListNode(nums[0]) # 头节点
    cur = head # 移动节点
    mid_loop = head # 在由结尾到中间之间成环 在i= 5 的时候成Loop
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next  # 指向 到 下一个节点
        if i == 12:
           mid_loop = cur  # 取 中间一个节点
    # cur.next = head # 这是形成完整的环

    # 还有一种是中间有一个环 （两者取其一）
    cur.next = mid_loop
    #
    return head  # 只要有了head 就可以将链表找到

def build_interval_list(nums): # 交叉链表
    head = ListNode(nums[0]) # 头节点
    cur = head
    mid_interval = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next
        if i == 18:
            mid_interval = cur

    second_list_head = ListNode(val=19)
    curr = second_list_head
    for i in range(20, 50):
        curr.next = ListNode(i)
        curr = curr.next
    curr.next = mid_interval

    return head, second_list_head


"""
快慢指针实现循环链表的判断****************************************************
"""

# num = [1,2,3,4,5,6]

# 首先我们创建一个链表 测试的时候我们用pytest
# linkList = build_l(num)

# 测试是否是循环链表
def is_Loop_List_or_Not(linkList):
    """
    测试是否是循环链表 打印输出值
    :param linkList:
    :return:
    """
    cur = linkList
    while cur is not None:
        print(cur.val)
        cur = cur.next


def isExitsLoop(linkList):
    """
    利用快慢指针进行判断 当两者相遇的时候则有环
    :param linkList:
    :return:
    """
    fast = linkList
    slow = linkList

    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("break")
            return True
    return False

# print(isExitsLoop(linkList))

"""
快慢指针实现中位数查找****************************************************
"""


def middleNode1(linkList):
    fast = linkList
    slow = linkList

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        print(fast.val)
        slow = slow.next

    if fast.next is not None:
        return slow.next.val  # 偶数的时候返回 下节点
    else:
        return slow.val
# *************************
def middleNode(linkList):
    fast = linkList
    slow = linkList

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 首先我们创建一个链表 测试的时候我们用pytest
# linkList = build_recurrent_list(num)
# is_Loop_List_or_Not(linkList) #  观察是否成环


def findEntryNode(linklist): # 成环检测

    fast, slow = linklist, linklist

    while True:
        fast = fast.next.next
        slow = slow.next
        if slow == fast: # 表示相遇
            # 将 fast 移动到head 然后以步长为2 进行移动 此时可以将再次相遇的节点返回
            newfast = linklist
            break

    while True:
        newfast = newfast.next
        slow = slow.next
        if slow == newfast:
            return slow.val

# print(findEntryNode(linkList))


head, second_list = build_interval_list(num)


def find_interval_in_doubleList(list1, list2):
    newlist1, newlist2 = list1, list2

    #将第一条链成环
    cur1 = newlist1
    count1 = 0
    while cur1.next != None:
        count1 +=1
        cur1 = cur1.next
    cur1.next = newlist1

    # 进一步检查 是否 有入口 并返回入口序号
    jiaodian = findEntryNode(newlist2)
    print(jiaodian)

# find_interval_in_doubleList(head, second_list)


# 单链表的逆转 k个
def singleListinverse(k, head):
    myhead = ListNode()
    myhead.next = head
    # 首先 定义三个指针
    new = myhead.next
    old = myhead.next.next

    count = 1
    while count < k:
        temp = old.next # 防止链表的丢失
        old.next = new
        # 然后进行移位操作
        new = old
        old = temp
        count += 1
    myhead.next.next = old
    return new


linklist = build_l(num)
pp = singleListinverse(1, linklist)
is_Loop_List_or_Not(pp)










