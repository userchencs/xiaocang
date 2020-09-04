# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:jingdian
# File_name:Demo01_if.py
# Author: chen chang song
# Time:2020年07月15日
# import easygui
# if True:
#     print("条件成立")
# print("条件成立2")      #没缩进不属于if，
# print("------------------------------------------1-")
# """
#  s = int(input("请输入你的年龄："))
#  if s >17:
#     print("你已经成年")
#  else:
#      print("你未成年")
# """
# s=easygui.enterbox(msg = "请输入你的性别",title = "请输入你的性别：")
# if s=="男":
#     print("你是：%s,请进入男澡堂"%s)
#     easygui.msgbox("你是：%s,请进入男澡堂"%s)
# elif s=="女":
#      print("你是:%s,请进入女澡堂"%s)
#      easygui.msgbox("你是:%s,请进入女澡堂"%s)
# else:
#     print(":%s,非法输入"%s)
#     easygui.msgbox(":%s,非法输入"%s)
#
# print("------------------------------------------2-")
#
# age =int(easygui.enterbox(msg = "年龄必须数字！！！",title = "请输入年龄数字："))
# if age<18:
#     print("你的年龄是：%d，你是童工"%age)
#     easygui.msgbox("你的年龄是：%d，你是童工"%age)
# elif age>=18 and age <=40:
#     print("你的年龄是：%d,你符合工龄"%age)
#     easygui.msgbox("你的年龄是：%d,你符合工龄"%age)
# elif age>40 and age<=60:
#     print("你的年龄是：%d，我们考虑一下"%age)
#     easygui.msgbox("你的年龄是：%d，我们考虑一下"%age)
# elif age>60:
#     print("你的年龄是：%d,你可以退休啦"%age)
#     easygui.msgbox("你的年龄是：%d,你可以退休啦"%age)
# print("------------------------------------------3-")
# w = input("请输入网吧或者公司")
# if w=="网吧":
#     print("你选择：%s"%w)
# else:
#     print("你选择：%s"%w)
#
# print("------------------------------------------4-")
# s =int(easygui.enterbox(msg = "输入分数！！！",title = "请输入分数数字："))
# if s >=90:
#     easygui.msgbox("%d分是优秀"%s)
# elif s>=60 and s<=70:
#     easygui.msgbox("%d分是及格" % s)
# elif s >= 80 and s <= 90:
#     easygui.msgbox("%d分是良好" % s)
# else:
#     easygui.msgbox("%d分是不及格" % s)
# print("------------------------------------------3-")
# s =int(input("0没钱，1有钱，输入你是否有钱："))
# if s==1:
#     print("有钱可以上车")
#     z = int(input("0没坐，1有坐，输入你是否有坐："))
#     if z==1:
#         print("坐吧")
#     else:
#         print("站着")
# else:
#     print("走路")
# print("------------------------------------------3-")