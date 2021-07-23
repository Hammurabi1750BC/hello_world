# 814	Binary Tree Pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def recurse2nodes(node):
            if not node:
                return False
            has1_left = recurse2nodes(node.left)
            if not has1_left:
                node.left = None
            has1_right = recurse2nodes(node.right)
            if not has1_right:
                node.right = None
            return node.val or has1_left or has1_right
                
        recurse2nodes(root)
        
        return root if root.val == 1 or root.left or root.right else None
