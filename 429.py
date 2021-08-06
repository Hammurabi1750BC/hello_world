# 429	N-ary Tree Level Order Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        levels = []
        
        q = deque([[0, root]])
        while q:
            height, node = q.popleft()
            if len(levels) <= height:
                levels.append([node.val])
            else:
                levels[height].append(node.val)
            for child in node.children:
                q.append([height+1, child])
        
        return levels
