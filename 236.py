# 236	Lowest Common Ancestor of a Binary Tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse2lca(node, lca, saw_p, saw_q):
            if not node:
                return node, saw_p, saw_q
            if lca:
                return lca, saw_p, saw_q
            
            l_lca, l_saw_p, l_saw_q = recurse2lca(node.left, lca, saw_p, saw_q)
            if l_lca:
                return l_lca, l_saw_p, l_saw_q
            r_lca, r_saw_p, r_saw_q = recurse2lca(node.right, lca, saw_p, saw_q)
            if r_lca:
                return r_lca, r_saw_p, r_saw_q

            saw_p = saw_p or l_saw_p or r_saw_p or node == p
            saw_q = saw_q or l_saw_q or r_saw_q or node == q
            
            if saw_p and saw_q:
                lca = node
                
            return lca, saw_p, saw_q

        
        return recurse2lca(node=root, lca=None, saw_p=False, saw_q=False)[0]
