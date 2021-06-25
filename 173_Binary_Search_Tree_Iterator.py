# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = deque([])
        self.stack2leftmost(root)
        

    def next(self) -> int:
        next_node = self.stack.pop()
        if next_node.right:
            self.stack2leftmost(next_node.right)
        
        return next_node.val
        

    def hasNext(self) -> bool:
        return self.stack

        
    def stack2leftmost(self, node):
        while node != None:
            self.stack.append(node)
            node = node.left
        
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
