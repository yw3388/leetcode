
# coding: utf-8

# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

# In[ ]:


from itertools import combinations
class Solution:
    def par(self, s):
        """k = []
        for i in range(1, len(s) + 1):
            
            for res in self.partition(s[i:]):
                if s[:i] == s[i-1::-1]:
                    alist = s[:i] + res
                    k.append(alist)
        return k"""
        start, end = 0, len(s)-1
        while start < end:
            
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
    def partition(self, curr, s):
        ##if no length
        if (len(s) == 0):
            result.append(curr[:])
            return
        for i in range(1, len(s) + 1):
            if self.par(s[:i]):
                #字母是正反相同
                ##检查到i-1为止，还需要检查是i开始，curr检查过的+list(检查过的string字母)
                self.partition(curr + [s[:i]], s[i:])
                
   
        result = []
        self.partition([], s)
        return result

