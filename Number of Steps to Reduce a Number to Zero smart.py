
# coding: utf-8

# 1342. Number of Steps to Reduce a Number to Zero
# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
# 
#  
# 
# Example 1:
# 
# Input: num = 14
# Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.

# In[6]:


##two steps to -1 and divide
##one step to divide and 1
def number(num):
    cnt = 0
    while num > 0:
        cnt += 2 if num != 1 or num % 2 == 1 else 1
        num //= 2 ##floor divide
    return cnt


# In[7]:


number(3)


# In[15]:


##count highest to lowest
"""
001010001
1: -1
2: right shift
3: right shift
...
n: -1
n+ 1: right shift
##right shift 1 for three
##count number of 0 to right shift
##0 left, so steps -1


"""
def count(c):
    nums = "{0:b}".format(c)
    k = nums.count('1') + len(nums) - 1
    return k

