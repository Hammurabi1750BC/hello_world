# 437	Path Sum III

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def recurse2sum(node, d_sums2date):
            num_paths = 0
            if node:
                d_next_sums = {key + node.val: val for key, val in d_sums2date.items()}
                d_next_sums[node.val] = d_next_sums.get(node.val, 0) + 1
                num_paths += d_next_sums.get(targetSum, 0)
                
                num_paths += recurse2sum(node.left, d_next_sums)
                num_paths += recurse2sum(node.right, d_next_sums)
            
            return num_paths
                    
        return recurse2sum(node=root, d_sums2date=dict())
