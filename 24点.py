
# coding: utf-8

# ##
# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
# 
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24

# In[77]:


def two(alist):
    i = False
    
    for k, j in itertools.permutations(alist, 2):
        for item in ['*', '-', '/', '+']:
            strs = str(k) + item + str(j)
            print(eval(strs))
            if np.isclose(eval(strs), 24, 0.01) == True:
                i =  True
                
            
           
    return i
             


# In[78]:


two([1, 23])


# In[80]:


#eval() 函数，接受一个字符串，能让这个字符串当成 python 代码运行，返回运行的结果。
eval('3 * 5')
alist = [4, 1, 8, 7]
itertools.zip_longest([2, 4, 5, 1], [4, 2, 6],  fillvalue = 0)
def two(alist):
    
    if len(alist) == 1:
        return np.isclose(eval(alist[0]), 24, 0.01)
    i = False
    for k, j, *_ in itertools.permutations(alist):
        for item in ['*', '-', '/', '+']:
            strs = str(k) + item + str(j)
            if two([strs]+ _) == True:
                i = True
            
           
    return i
             
        
        
    


# In[81]:


two(alist)


# In[37]:


import numpy as np
import itertools
def judgePoint24(nums):
    if len(nums) == 1:
        return np.isclose([nums[0]], [24], 0.01)
    ##replace two elements with any operation of these 
    ##division and subtract are not permutable
    ##use recursive to replace the smaller lists
    ##any will return True if any of the list is True
    #if b is 0 then b ane a/b will do the job
    return any(judgePoint24([k] + res) for a, b, *res in itertools.permutations(nums)for k in [a*b, a+b, a-b, b and a/b])
        


# In[28]:


judgePoint24([2, 4, 6, 2])


# In[25]:


nums = [2, 4, 5, 6, 10]
for a, b, *res in itertools.permutations(nums):
    #print([a, b, res])
    for k in [a*b, a+b, a-b, b and a/b]:
        newlist = [k] + res
        print(newlist)
   


# In[29]:


##make every combinations and permutations of element and operation
itertools.product([3, 4, 5, 1]) 

