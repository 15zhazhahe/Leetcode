# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        def dfs(node):
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            ans[0] = max(ans[0], l + r)
            return max(l, r) + 1
        dfs(root)
        return ans[0]