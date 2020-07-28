
# coding: utf-8

# Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
# 
# Return the sorted array.
# 
#  
# 
# Example 1:
# 
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]

# Input
# [10000,10000]
# 
# Output
# [10000]
# 
# Expected
# [10000,10000]

# In[2]:


class Solution:
    def sortByBits(self, arr):
        #ord(number)
        #2**n + 2**(n-1)+mod
        """ def get_ones(number):
            c = 0
            if number % 2 == 1:
                number -= 1
                c += 1
            for n in range(number+1, 1, -1):
                if number == 2 ** n:
                    c += 1
                    break
            for n in range(number+1, 1, -1):
                if number > 2 ** n:
                    number -=  2 ** n
                    c += 1
            return c"""
        """ def get_ones(number):
            k = 0
            while number:
                k = 1 & number
                number << 2
            return k"""
        arr = sorted(arr)
        alist = [bin(number).count('1') for number in arr]
            
        #alist = list(map(get_ones, arr))
        d = sorted(dict(zip(arr, alist)).items(), key = lambda x:x[1])
        
        return [dd[0] for dd in d]
            


# In[4]:


##别人一行的代码
def sortByBits(self, arr):
    return sorted(sorted(arr), key=lambda x: bin(x).count('1'))

