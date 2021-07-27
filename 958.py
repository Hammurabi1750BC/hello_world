# 958	Check Completeness of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

# v2
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = deque([root])
        gap = False
        while q:
            node = q.popleft()
            if node == None:
                gap = True
            elif gap:
                return False
            else:
                q.append(node.left)
                q.append(node.right)
        
        return True


# v1
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return root
        
        level = [root]
        no_lr = False
        while level:
            next_level = []
            for node in level:
                if node.left:
                    if no_lr:
                        return False
                    next_level.append(node.left)
                else:
                    no_lr = True
                
                if node.right:
                    if no_lr:
                        return False
                    else:
                        next_level.append(node.right)
                else:
                    no_lr = True
            level = next_level
        
        return True
