
# coding: utf-8

# In[ ]:


Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.


# In[ ]:


import numpy as np
class Solution:
    ##从左到右减小，从上到下减小
    ##从左下开始
    def countNegatives(self, grid: List[List[int]]) -> int:
        #g = np.array(grid).flatten()
        #return int(np.sum([1 for x in g if x < 0]))
        
        ##method2
        """
        n = len(grid[0]) 
        r, c, cnt = len(grid)-1, 0, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                cnt += n - c 
                r -= 1
            else:
                c += 1
        return cnt
        """
        ##method3 从右往左从上往下
        ##右上角小，上面的row都是小的，r, 大的话就col往左移动
        n = len(grid)
        r, c, cnt = 0, len(grid[0])-1, 0
        while r < n and c >= 0:
            if grid[r][c] < 0:
                cnt += n - r
                c  -= 1
            else:
                r += 1
        return cnt
        
        

