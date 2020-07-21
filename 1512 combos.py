
# coding: utf-8

# Given an array of integers nums.
# 
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# 
# Return the number of good pairs.
# 
#  
# 
# Example 1:
# 
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# In[ ]:


##combinations:n * (n-1)/2
import collections
import itertools
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        alist = collections.Counter(nums)
        cnt = 0
        for v in alist.values():
            k = [1] * v
            a = len(list(itertools.combinations(k, 2)))
            cnt += a
            
        return cnt


# In[ ]:


def numIdenticalPairs(self, nums: List[int]) -> int:
        set_nums=set(nums)
        good=0
        for x in set_nums:
            n=nums.count(x)
            good+=(n*(n-1))/2 
#finding number of occurences of element and using nC2 to find good pairs 
        return int(good)

