
# coding: utf-8

# ## 海伦公式
# ## S=√p(p-a)(p-b)(p-c
# 812. Largest Triangle Area
# Easy
# 
# 188
# 
# 977
# 
# Add to List
# 
# Share
# You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.
# 
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: 
# The five points are show in the figure below. The red triangle is the largest.

# In[2]:


import itertools

class Solution:
    def largestTriangleArea(self, points):
        
        def hellon(a, b, c):
            aa = ((a[0]-b[0])**2 + (a[1] - b[1]) **2)**0.5
            bb = ((a[0]-c[0])**2 + (a[1] - c[1]) **2)**0.5
            cc = ((b[0]-c[0])**2 + (b[1] - c[1]) **2)**0.5
            k = 0.5 * (aa + bb + cc)
            return k * (k - aa) * (k - bb) * (k - cc)
        
        return max(hellon(*d) for d in itertools.combinations(points, 3))**0.5


# In[3]:


#Heron's formula
#area = 0.5 * a * b * sin(C)
class Solution(object):
    def largestTriangleArea(self, points):
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))

