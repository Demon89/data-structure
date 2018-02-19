# _*_coding: utf-8_*_
"""
-------------------------------------------------
   File Name：     多个无序列表排序
   Description :
   Author :        demon
   date：          19/02/2018
-------------------------------------------------
   Change Activity:
                   19/02/2018:
-------------------------------------------------
"""
__author__ = 'demon'
import cProfile
from functools import wraps
from random import randint


# def merge_seq(func):
#     @wraps(func)
#     def wrapper(*args, temp=None):
#         if not temp:
#             temp = []
#         for seq in args:
#             if not isinstance(seq, (list, int)):
#                 return 'Low B brother, parameter args must be iterator'
#         if len(args) < 2:
#             result = func(args[0])
#         else:
#             for seq in args:
#                 if isinstance(seq, abc.Iterable):
#                     temp.extend(seq)
#                 else:
#                     temp.append(seq)
#             result = func(temp)
#         return result
#     return wrapper

# 装饰器，用于合并快速排序中的参数的，也就是可以支持任意个参数，但是参数类型只限于list,tuple和int
def merge_seq(support_int=True):
    def wrapper(func):
        @wraps(func)
        def inner(*args, temp=None):         # args支持任意个参数，但是要判断支持的参数类型，需要使用for循环迭代并且通过isinstance来判断参数的类型
            if not temp:                     # 如果temp没有给参数，就使用默认的空列表，这个参数会作为快速排序中形参传递
                temp = []
            if len(args) < 2 and isinstance(args[0], int):  # 如果传递进来的参数小于2个，并且参数不是int类型，就原样返回结果
                return args[0]
            else:
                if support_int:              # 三层装饰其中需要判断的是否支持参数直接传递int类型进行排序，默认参数为支持
                    error_msg = 'Low b brother, parameter must be list tuple or int'
                    for seq in args:
                        if isinstance(seq, (tuple, list)):  # 判断每个参数，如果参数类型是list或者tuple，则可以通过列表中的extend方法把可迭代对象添加到temp列表中
                            temp.extend(seq)
                        elif isinstance(seq, int):          # 如果为int类型，可以使用append方法，直接添加到temp列表中
                            temp.append(seq)
                        else:                               # 如果以上的类型都不满足，则返回一个错误，并告知支持的参数类型
                            return error_msg
                else:
                    error_msg = 'Low b brother, parameter must be list or tuple'
                    for seq in args:
                        if isinstance(seq, (tuple, list)):
                            temp.extend(seq)
                        else:
                            return error_msg
                result = func(temp)        # 调用快速排序算法，进行多个参数对象的快速排序，这里的func即为quick_sort函数
                return result
        return inner
    return wrapper


@merge_seq()
def quick_sort(seq):     # 快速排序算法
    if len(seq) < 2:
        return seq
    else:
        num = seq[0]
        less_num_seq = [i for i in seq[1:] if i <= num]
        bigger_num_seq = [i for i in seq[1:] if i > num]
        finally_num_seq = quick_sort(less_num_seq) + [num] + quick_sort(bigger_num_seq)
        return finally_num_seq


def main(*args):
    result = quick_sort(*args)
    cProfile.run('quick_sort({})'.format(*args))
    if isinstance(result, list):
        print('quick sort numbers', result)
    else:
        print('\033[31m{}\033[0m'.format(result))


if __name__ == "__main__":
    l1 = [randint(1, 100000) for _ in range(5)]
    l2 = [randint(1, 1000000) for _ in range(5)]
    main(l1, 10, -2, l2, 20, -5)