
# coding: utf-8

# ##64 sqrt(x)
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# In[5]:


##Newton's Method
##rn+1 = rn - f(rn)/f'(rn)
##r**2 - x = 0, so rn+1 = rn - (r**2-x)/2r

class Solution:
    def mySqrt(self, x: int):
   
         
        r = x + 1  # avoid dividing 0
        while r * r > x:
            r = int(r - (r*r - x)/(2*r))  # newton's method
        return r
    
    


# In[ ]:


##binary search

