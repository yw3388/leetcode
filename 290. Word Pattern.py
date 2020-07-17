
# coding: utf-8

# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
##加入字典中时候要区分来自哪一个，可能值一样
#对应的pattern要在string中
#如果出现pattern不符合就是false
#学会了map(string.find, string）的方法


def wordPattern(pattern: str, str: str):
    dic = {}
    # a list of words
    words = str.split(' ')
    # patter is a list of string
    #make a dictionary of two keys and one value
    #if value not equal to another value
    if len(pattern) != len(words):
        return False
    for i in range(len(words)):
        c = pattern[i]
        w = words[i]
        if c not in dic:
            dic[c] = i
        if w not in dic:
            dic[w] = i
        if dic[c] != dic[w]:
            return False
    return True
            


# In[9]:



def wordPattern(pattern: str, str: str) -> bool:
    dic = {}
    # a list of words
    words = str.split(' ')
    # patter is a list of string
    #make a dictionary of two keys and one value
    #if value not equal to another value
    if len(pattern) != len(words):
        return False
    for i in range(len(words)):
        c = pattern[i]
        w = words[i]
        print(c)
        print(w)
        c = 'v{}'.format(c)
        w = 'w{}'.format(w)
        print(c)
        if c not in dic:
            dic[c] = i
        if w not in dic:
            dic[w] = i
        if dic[c] != dic[w]:
            return False
    return True


# In[10]:


pattern = "abba"
str = "dog cat cat dog"
wordPattern(pattern, str)


# In[ ]:


map(pattern.find, pattern)== map(string.index, string)  

