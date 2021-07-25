# 129. Sum Root to Leaf Numbers
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def recurse2leaves(node, sum2date):
            if node:
                sum2date += str(node.val)
                if not node.left and not node.right:
                    r2lnums.append(int(sum2date))
                else:
                    recurse2leaves(node.left, sum2date)
                    recurse2leaves(node.right, sum2date)            
            
        r2lnums = []
        recurse2leaves(node=root, sum2date='')
        
        return sum(r2lnums)
