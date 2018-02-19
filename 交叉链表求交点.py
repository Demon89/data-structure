# _*_coding: utf-8_*_
"""
-------------------------------------------------
   File Name：     交叉链表求交点
   Description :
   Author :        demon
   date：          18/02/2018
-------------------------------------------------
   Change Activity:
                   18/02/2018:
-------------------------------------------------
"""
__author__ = 'demon'

a = [1, 2, 3,  7, 9, 1, 2, 5]
b = [4, 5, 7, 9, 1, 2, 5]

for index, (x, y) in enumerate(zip(reversed(a), reversed(b)), 1):
    if x ^ y:
        position = index - 1
        if position == 0:
            print('玩个球球~~~')
            break
        intersection = a[-position]
        print('交叉点为:', intersection)
        break
