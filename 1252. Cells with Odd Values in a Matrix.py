
# coding: utf-8

# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.
# 
# Return the number of cells with odd values in the matrix after applying the increment to all indices.
# 
#  Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

# In[40]:


import collections
def oddCells( n: int, m: int, indices):
    d =[[0] * m] * n
    cnt = 0
    alls = [item[0] for item in indices]
    cols = [item[1] for item in indices]
    print(alls)
    print(cols)
    dd= collections.Counter(alls)
    qq = collections.Counter(cols)
    print(qq)
    for i in range(n):
        if i in dd.keys():
            d[i] = [dd[i]] * m
   
        for j in range(m):
            if j in qq.keys():
                d[i][j] += qq[j] 
                print(d[i][j])
    for i in range(n):
        for j in range(m):
            if d[i][j] % 2 != 0:
                cnt += 1


    return cnt


# In[41]:


n = 2
m = 3
indices = [[0,1],[1,1]]
oddCells(n, m, indices)


# In[42]:



n = 48
m = 37
indices = [[40,5]]
oddCells(n, m, indices)


# In[43]:



n = 41
m = 38
indices = [[38,33],[37,24],[33,6],[15,0],[13,22],[1,13],[12,8],[20,4],[30,9],[21,0],[35,29],[21,20],[36,24],[40,16],[3,24],[32,6],[19,28],[1,13],[30,19],[28,20],[28,2]]


# In[44]:


oddCells(n, m, indices)


# In[53]:


def oddCells( n: int, m: int, indices):
    rows, cols = [False] * n, [False] * m
    for r, c in indices:
        ##第r行，第c列
        rows[r] ^= True
        cols[c] ^= True
    return sum([row ^ col for row in rows for col in cols])


# In[75]:


import itertools
n = 41
m = 38
indices = [[38,33],[37,24],[33,6],[15,0],[13,22],[1,13],[12,8],[20,4],[30,9],[21,0],[35,29],[21,20],[36,24],[40,16],[3,24],[32,6],[19,28],[1,13],[30,19],[28,20],[28,2]]
oddCells(n, m, indices)


# In[74]:


"""def oddCells( n: int, m: int, indices):
    rows, cols = [False] * n, [False] * m
    cnt_r, cnt_c = 0, 0
    for r, c in indices:
        ##第r行，第c列
        rows[r] ^= True
        cols[c] ^= True
        ##奇数次的行奇数次的列 else -1
        cnt_r += 1 if rows[r] == True else 0
        cnt_c += 1 if cols[c] == True else 0
        ##多少次的cell减去共同算的(不是共同算的而是变成了even)减去even
    return cnt_r * m +  cnt_c * n - 2 * cnt_r * cnt_c """

