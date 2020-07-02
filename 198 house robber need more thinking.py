
# coding: utf-8

# 198. House Robber
# Easy
# 
# 4705
# 
# 143
# 
# Add to List
# 
# Share
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
# 
#  
# 
# Example 1:
# 
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
# 
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

# ##不能连续两个相加求最大子序列问题
# ## 一开始想奇偶，但是可以步长4
# ##def rob(self, nums: List[int]) -> int:
#         ##n = 4, nums start points can be 4
#         length = len(nums)
#         m = 0
#         for i in range(1, length):
#             sums = int(sum(nums[::int(i)]))
#             if sums > m:
#                 m = sums
#         return m
# ##答案错误
# ##为啥可以recursive
# class Solution:
#     
#     def rob(self, nums):
#         
#         last, now = 0, 0
#         
#         for i in nums: last, now = now, max(last + i, now)
#                 
#         return now
