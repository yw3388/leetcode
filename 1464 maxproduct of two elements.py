
# coding: utf-8

# In[2]:


import itertools
import math
class Solution:
    def maxProduct(self, nums):
        """
        n = [k - 1 for k in nums]
        return max(list(map(math.prod, (itertools.combinations(n, 2)))))
        """
        ##largest and second largest
        m = n = -math.inf
        for num in nums:
            if num > m:
                n = m
                m = num
            elif num > n:
                n = num
            
        return (m - 1)*(n - 1)

