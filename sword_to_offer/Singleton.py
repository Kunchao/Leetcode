#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/8
# @Author  : Vapor

# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_the_instance'):
#             cls._the_instance=object.__new__(cls,*args, **kwargs)
#         return cls._the_instance
#
# class A(Singleton):
#     print('init before')
#     def __init__(self):
#         print('i am __init__')
#     def f(self):
#         print('i am f')
#
# a=A()
# b=A()
# a.f()
# print('done')

# import time
# import threading
# class Singleton(object):
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         time.sleep(1)
#
#     @classmethod
#     def instance(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance
#
#
# def task(arg):
#     obj = Singleton.instance()
#     print(obj)
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()
# time.sleep(20)
# obj = Singleton.instance()
# print(obj)

# import time
# import threading
#
# class Singleton(object):
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         time.sleep(2)
#         # pass
#
#     @classmethod
#     def instance(cls, *args, **kwargs):
#         with Singleton._instance_lock:
#             if not hasattr(Singleton, "_instance"):
#                 Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance
#
# import threading
#
# def task(arg):
#     obj = Singleton.instance()
#     print(obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()
#
# time.sleep(20)
# obj = Singleton.instance()
# print(obj)

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass(Singleton):
    pass