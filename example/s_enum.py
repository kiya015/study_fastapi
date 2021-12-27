#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
@author:huiling.chen
@file: s_enum.py 
@time: 2021/12/27 15:07 
"""

from enum import Enum


class Color(Enum):
    # 为序列指定value值
    red = 1
    green = 2
    bule = 3


# class test(object):
#     name = "kiya"

if __name__ == '__main__':
    # print(dir(test))
    # result = test()
    # print(dir(result))
    # 调用枚举成员的3种方式
    print('1', Color.red)
    print('2', Color['red'])
    print('3', Color(1))
    # 调用枚举成员中的value 、name
    print('4', Color.red.value)
    print('5', Color.red.name)
    # 遍历枚举类中所有成员的2种方式
    for color in Color:
        print(color)
    # 枚举类成员之间不能比较大小，但可以用 == 或者 is 进行比较是否相等，例如：
    print(Color.red == Color.green)
    print(Color.red.name is Color.green.name)