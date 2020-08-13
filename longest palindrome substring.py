
# coding: utf-8

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# 
# Example 1:
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# In[44]:


import math
def center(s, left, right):
    #pass two indices, left starting from left index and right starting from right index
    #make sure two indices is larger than 0 and smaller than the last index
    l = left
    r = right
    #boundary: left, right, equal value
    #all longest substring with indices between left and right
    while l >= 0 and r < len(s) and s[l] == s[r]:
        
        r += 1
        l -= 1
       
    return r - l - 1

s = 'bababd'
center(s, 1, 1)
#get between two indices the longest substring's length


# In[58]:


#find start and end index(same in the beginning) of string for the longest substring of whole string starting, update from start and end
# function of string, start, end
#i, i = 0, 0
#for eaach index i, start from i, i, then has substring larger than 0, (i, i - 1, i + 3/2); 
def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        
        if s is None and len(s) < 1:
            return ''
        start = 0
        end = 0
        
        
        
        for i in range(0, len(s)):
            ##length with string, index i and index i if odd length
            len1 = center(s ,i, i)
            ##length iwth string, index i and i + 1 if even length
            len2 = center(s, i, i+1)
            m = max(len1, len2)
            #locate end and start in string, with pandrome in index of string increases
            #and decreases
            print(m)
            print(start)
            print("end:" + str(end))
            print(s[start:end+1])
            #start from 0, enlarge index
            #end = 0 + 2
            #start= 0 - 1.5 = -1
            if m > end - start:
                start = math.ceil(i - (m-1)/2)
                end = int(i + m/2)
        return s[start:end+1]
            
    


# In[59]:


s = "bab"
longestPalindrome(s)

