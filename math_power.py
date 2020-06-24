# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:09:34 2020

@author: yw338
"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n /= 3
        if n == 1:
            return True
        else:
            return False
    
    
    ##solution two##if we convert our number to base 3 and the representation 
    #is of the form 100...0, then the number is a power of 3.
     
        
    ##solution three: 3** k = n, log10(n)/log10(3) ---(k) is an integer
        
     ##solution four:   
    def isPowerOfThree(self, n: int) -> bool:
        #1162261467 = floor( LARGEST_INT_SUPPORTED / 3 ) * 3 
         ##greatest integer power of 3
        return  n > 0 and 1162261467 % 3 == 0
    