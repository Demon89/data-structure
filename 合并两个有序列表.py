# _*_coding: utf-8_*_
"""
-------------------------------------------------
   File Name：     合并两个有序列表
   Description :
   Author :        demon
   date：          18/02/2018
-------------------------------------------------
   Change Activity:
                   18/02/2018:
-------------------------------------------------
"""
__author__ = 'demon'

from itertools import zip_longest
result = []
a = [0, 3, 5, 8, 100, 140, 180, 230]
b = [1, 9, 13]

# case 1
import bisect


def sort_list(a, b, result=None):
    if not result:
        result = []
    for x in a:
        bisect.insort(result, x)
    for y in b:
        bisect.insort(result, y)
    return result


print(sort_list(a, b))


# case 2
def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)


def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])


print(recursion_merge_sort2(a, b))
