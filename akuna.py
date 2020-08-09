
# coding: utf-8

# number of transactions/sec <= 3
# number of transactions/10 secs <= 20
# number of transactions/60 secs <= 60
# drop an integer that is total number of dropped requests

# In[1]:


alist = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 11, 11, 11, 6, 6, 6, 5, 5, 5]


# In[2]:


import collections


# In[22]:


d = collections.Counter(alist)
d2 = dict(sorted(d.items(), key = lambda x:x[0]))
cumsum = dict()
cumsum[0] = list(d2.values())[0]
drops = 0
for i in range(1, list(d2.keys())[-1]+1):
    if i in d2.keys():
        if d2.get(i) > 3:
            drops += d2.get(i) - 3
            cumsum[i] = 3 + cumsum[i-1]
        else:
            cumsum[i] = d2.get(i) + cumsum[i-1]
    else:
        cumsum[i] = cumsum[i-1]
print(cumsum)

for key, value in cumsum.items():
    
    if key + 10 in cumsum.keys():
        if cumsum[key+10] - cumsum[key] > 20:
            drops += cumsum[key+10] - cumsum[key] - 20
            cumsum[key + 10] = cumsum[key] + 20
    if key + 60 in cumsum.keys():
        if cumsum[key + 60] - cumsum[key] > 60:
            drops += cumsum[key+60] - cumsum[key] - 60
            cumsum[key + 60] = cumsum[key] + 60
drops
        


# give a string and a series of queries
# each query: starting index and ending index and number of substitution
# can reorder string and determine if string can be changed into a palindrome in a given number of substitutions 
# 'c', key = 0, return '1'
# 'cd', key = 1, return '11', append 1
# substring = 'cde', key =1 , can substitude e to c, return '111', append 1
# substring = 'cded', key = 0, cannot substitude, return '1110'
# 

# In[ ]:


n, q = [int(i) for i in input().split()]
s = input()


# ## split a string into pieces(string, k), order of substrings is not changed, and can be empty
# ## no repete elements in substrings
# # print yes if can be split in this way

# In[104]:


k = 2
numbers = [1, 2, 4, 6]
[[1, 2], [1, 4], [2, 4], [2, 6], [4, 6], [1, 6], []]
[1, 2] + [4, 6] 


# In[58]:


k = 2
numbers = [1, 2, 2, 3, 4, 6]

from itertools import combinations
alist = list(combinations(numbers, k))
for i in range(len(alist)):
    for j in range(i+1, len(alist)):
        if list(alist[i]) == list(set(alist[i])) and list(alist[j]) == list(set(alist[j])) and list(alist[i]) + list(alist[j]) == numbers:
            print('yes')
        else:
            if list(alist[i]) == numbers:
                print('yes')


# In[106]:


q = [list(element) for element in alist]
a = [numbers] * len(q)


def rec(a, q):
    z = []
    for i in range(0, len(q)):
        c = [element for element in a[i] if element not in q[i]]
        rec(a,c)
        z.append(c)
    return z


# In[150]:


aa = a[4]
qq = q[4]
def rec(aa, qq, k):
    
    if len(qq) == k:
        return qq
    else:
        c = [element for element in aa if element not in qq]
       
        return rec(aa, c, k)
            
    
        
        
    


# In[149]:


#[aa + qq == numbers for aa, qq in zip(a, rec(a, q))]
for aa, qq in zip(a, q):
    print(rec(aa, qq, 2))


# average < 25%, reduce by half
# 25% <= average <= 60%, no
# average > 60%, double if not > 2 * 10 ** 8
# 

# In[102]:


#avg = [25, 23, 1, 3, 4, 5, 10, 29]
import math
stop = 10
ins = 2
i = 0
a = avg[i]
while i <= len(avg):
    a = avg[i]
    if a < 25:
        ins = math.ceil(ins/ 2)
        i += 10
    elif a > 60:
        ins *= 2
        i += 10
    else:
        i += 1
    print(ins)


# In[87]:


avg = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]

