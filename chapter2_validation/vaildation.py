#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:01:26 2019

@author: hienh
"""

###############Task1############
#With a new line:
print ("What’s your age?")
Age = input()
#With a space:
Age = input("What’s your age? ")
#output data type is stringß

###############Task2############

print ("What’s your age?") 
age = int(input()) 
type(age)

###############Task3############

Option = input("Please input yes or no ").lower()
Option = input("Please input yes or no ").upper()

###############Task4############

number = ''
while len(str(number)) != 11:
    try:
        number = int(input("what is your phone number? "))
    except ValueError:
        print("invalid phonenumber, please check")
        number = ""
    
###############Task5############

print('***choice****') 
print('1. Display my name') 
print('2. Display my age') 
print('3. Display my city')
choice = 0


while choice < 1 or choice > 3:
    try:
        choice = int(input('What is your choice? '))
    except ValueError:
        print("invalid choice")
    else:
        if choice < 1 or choice > 3:
            print('not in range')

if choice == 1:
    print('Ms Wu')
elif choice == 2:
    print('5 years old')
elif choice == 3: 
        print('London')
    

###############Task6############

while True:
    choice = 0

    try:
        while choice< 1 or choice > 3:
            choice = int(input('What is your choice?'))
            if choice == 1:
                print('Ms Wu')
            elif choice == 2:
                print('5 years old')
            elif choice == 3: 
                print('London')
       
            break 
    except ValueError:
        print('please type a number! ')
    else:
        if choice < 1 or choice > 3:
            print('not in range')

###############Task7############
class Spam(object):
    def __init__(self, description, value):
        if not description or value <=0: 
            raise ValueError
        self.description = description 
        self.value = value

s = Spam('s', 5)
print(s.value)
print(s.description)
fs = Spam('', -1)

class Spam(object):
    def __init__(self, description, value):
        assert description != ""
        assert value > 0
        self.description = description 
        self.value = value

s = Spam('s', 5)
print(s.value)
print(s.description)
fs = Spam('', -1)