# _*_coding: utf-8_*_
"""
-------------------------------------------------
   File Name：     链表对调
   Description :
   Author :        demon
   date：          18/02/2018
-------------------------------------------------
   Change Activity:
                   18/02/2018:
-------------------------------------------------
"""
__author__ = 'demon'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head