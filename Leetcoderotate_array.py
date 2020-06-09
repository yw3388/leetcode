
# coding: utf-8

# Rotate to the right k times
# 
# 
# 
# 
# 
# 
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# In[3]:


##first solution
class Solution:
    def rotate(self, nums, k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k%len(nums)) :]+ nums[:-(k%len(nums)) ]


# In[4]:


##index i is (i+k)%length of array
def rotate(nums, k):
    n = len(nums)
    a = [0] * n
    for i in range(n):
        a[(i+k)%n] = nums[i]
    
    nums[:] = a

