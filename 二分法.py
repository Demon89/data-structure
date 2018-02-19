# _*_coding: utf-8_*_
"""
-------------------------------------------------
   File Name：     二分法
   Description :
   Author :        demon
   date：          18/02/2018
-------------------------------------------------
   Change Activity:
                   18/02/2018:
-------------------------------------------------
"""
__author__ = 'demon'

my_list = [1, 3, 5, 7, 8]


def binary_search(find_num, find_items=None):
    if find_items is None:
        return False

    low = 0
    high = len(find_items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess_num = find_items[mid]
        if find_num < guess_num:
            high = mid - 1
        elif find_num > guess_num:
            low = mid + 1
        else:
            return '您查找的{}在列表中的索引值为:{}'.format(find_num, mid)
    return '你要找的数字{}没有在此列表中'.format(find_num)


result = binary_search(5, my_list)
print(result)