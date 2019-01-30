#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:06:15 2019

@author: hienh
"""

###########Task 2######
  
#def is_prime(number):
#    #Return True if *number* is prime.
#    if number in (0, 1):
#        return False
#    for element in range(2, number):
#        print(number, element)
#        if number % element == 0:
#            return False
#        
#    return True

    
def print_next_prime(number):
#Print the closest prime number larger than *number*.
    index = number 
    while True:
        index += 1
        if is_prime(index):
            print(index)


###########Task 3######
def is_prime(number):
    #Return True if *number* is prime.
    if number <=1:
        return False
    for element in range(2, number):
        print(number, element)
        if number % element == 0:
            return False
        
    return True