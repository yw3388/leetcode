
# coding: utf-8

# 145 Binary Tree PostOrder Tranversal
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# Output: [3,2,1]

# In[3]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode):
        traversal, nodes = [], [root]
        while nodes:
            node = nodes.pop()
            if node:
                traversal.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
        return traversal[::-1]

