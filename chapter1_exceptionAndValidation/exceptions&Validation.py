#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:58:36 2019

@author: hienh
"""

####################TASK1###########################
#try:
#    f = open('testfile')
#except Exception: 
#    print('Error!')
#
#
#try:
#    f = open('testfile')
#except Exception:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
#
#
#
#
#####################TASK2###########################
#
#
#try:
#    f = open('testfile.txt')
#    s1 = not_exsit 
#except FileNotFoundError:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.') except Exception:
#    print('Sorry. Something is wrong after opening function.’)
#
#
#####################TASK3###########################
#
#
#try:
# f = open('testfile.txt')
# s1 = not_exists
#except Exception as e:
#    print(e)
#
#
#####################TASK4###########################
#
#try:
# f = open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close
#
#    
####################TASK5###########################
#   
#try:
# f = open('testfile')
#except Exception as e:
# print(e)
#else:
# print(f.read())
# f.close()
#finally:
# print('Executing finally…')
# 
# 
#try:
# f = open('testfile.txt')
#except Exception as e:
# print(e)
#else:
# print(f.read())
# f.close()
#
#finally:
# print('Executing finally…')
# 
 ###################TASK6###########################
#try:
#    f = open('testfile.txt')
#    if f.name == 'testfile.txt': 
#        raise Exception
#except Exception as e:
#    print('file name are the same')
