
# coding: utf-8

# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

# In[ ]:


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        bs = "{0:b}".format(n)
        return sum([int(i) for i in bs])
        """
    ##检查所有32bits的数字，如果是1，加上
    ##bit mask: m=1, AND: number and mask 1: least significant bit of the number
    #用and检查00000001， 00000010，etc
    ##integer 有32bit的代表
        """
            bits, mask = 0, 1
            for i in range(0, 32):
                if n & mask != 0:
                    bits += 1
                mask <<= 1
            return bits 
        """
        ##shift 1 to 0 if 0, then sums += 1
        ##找n表达式里面非0的部分
        ##n & (n-1)找到最后一位是1的部分，0&1=1
        ##n变n-1
        ##直到n的表达式中没有1的存在，即n=1
        sums = 0
        while n != 0:
            sums += 1
            n &= (n-1)
        return sums
          
            

