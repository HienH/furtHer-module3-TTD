#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:52:39 2019

@author: hienh
"""


class Calculator(object):
    def add(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types): 
            return x + y
        else:
            raise ValueError
    