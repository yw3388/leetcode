
# coding: utf-8

# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
# 
# Given n, find the total number of full staircase rows that can be formed.
# 
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
# 
# Example 1:
# 
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.

# ## 序列求和问题
# The Coins are arranged in the following way:
# [1,2,3,4,5....]
# This is an arithmetic sequence. To find the sum S of an arithmetic series , the formula is :
# S = ((a + b)* h) /2
# a = 1
#  b = h
# The equation can then be simplified into:
# S = (1 + h)*h / 2
# 
# (1 + h)*h / 2 <= n

# In[2]:


import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
       
        while left <= right:
            mid = (left + right)//2
            if mid * (mid + 1)//2 == n:
                return mid
            if mid * (mid + 1)//2 > n:
                right = mid - 1
            if mid *(mid + 1)//2 < n:
                left = mid + 1
        return  right


# In[3]:


### problems
# remember to change in the while loop
# floor division
# return right not left or mid or math floor of left, don't know about the cornerstone case


# ### If we look deeper into the formula of the problem, we could actually solve it with the help of mathematics, without using any iteration.
# This could be solved by completing the square technique.
