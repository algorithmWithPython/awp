class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        res = root.val
        def maxpath(tree):
            if not tree:
                return 0
            v = tree.val
            l, r = 0, 0
            if tree.left:
                l = maxpath(tree.left)
            if tree.right:
                r = maxpath(tree.right)
            nonlocal res
            res = max(res, v, v+l, v+r, v+l+r)
            return max(v, l+v, r+v)
        maxpath(root)
        return res