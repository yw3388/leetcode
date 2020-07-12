
# coding: utf-8

# 1266. Minimum Time Visiting All Points
# 
# 
# On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.
# 
# You can move according to the next rules:
# 
# In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.

# ![image.png](attachment:image.png)

# In[12]:


##pop:list of list
##NOT SURE about method one: the max step of previous one, 不一定是在同一个dimension


# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds

# In[6]:


import numpy as np

def minTimeToVisitAllPoints(points):
        
        ##vertically horizally 
         
         
    differences = abs(np.diff(points, axis = 0))
    sums = np.sum(differences, axis = 0)
    return max(sums)


# In[11]:


points = [[2, 4], [5, 6], [-1, 8]]
differences = abs(np.diff(points, axis = 0))
sums = np.sum(differences, axis = 0)
sums


# In[3]:


class Solution:
    def minTimeToVisitAllPoints(points):        
        d = 0
        x1, y1 = points.pop()
        while points:
       
            x2, y2 = points.pop()
            d += max(abs(x2 - x1), abs(y2 - y1))
            x1, y1 = x2, y2
        return d

