#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:53:38 2019

@author: hienh
"""

import unittest
from wordcount import wordcounter

class TestUnit(unittest.TestCase):
    
    def test_wordcounter(self):
        self.assertDictEqual(
            {'foo' : 2, 'bar' : 1},
            wordcounter('foo bar foo '))
        
        self.assertNotEqual({'foo' : 2, 'bar' : 1},
            wordcounter('foo bar foo '))
    
    
if __name__ == '__main__': 
    unittest.main()
    