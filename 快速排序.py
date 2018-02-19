# _*_coding: utf-8_*_
"""
-------------------------------------------------
   File Name：     快速排序
   Description :
   Author :        demon
   date：          18/02/2018
-------------------------------------------------
   Change Activity:
                   18/02/2018:
-------------------------------------------------
"""
__author__ = 'demon'


def quicksort(seq):
    if len(seq) < 2:
        return seq
    else:
        mid_pivot = seq[0]
        less_before_mid_pivot = [i for i in seq[1:] if i <= mid_pivot]
        bigger_after_mid_pivot = [i for i in seq[1:] if i > mid_pivot]
        print('less:', less_before_mid_pivot)
        print('bigger:', bigger_after_mid_pivot)
        finally_list = quicksort(less_before_mid_pivot) + [mid_pivot] + quicksort(bigger_after_mid_pivot)
        print('finally:', finally_list)
        return finally_list


print(quicksort([2, 4, 6, 7, 1, 2, 5]))
