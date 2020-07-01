
# coding: utf-8

# 1281. Subtract the Product and Sum of Digits of an Integer
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
#  

# In[ ]:


import numpy as np
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        A = list(map(int, str(n)))
        return reduce(operator.mul, A) - sum(A)
   

