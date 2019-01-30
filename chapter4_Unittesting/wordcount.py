#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:46:54 2019

@author: hienh
"""

def wordcounter(string):
    my_dict = {}
    for word in string.lower().split():
        my_dict[word] = string.count(word)

    return my_dict
        
