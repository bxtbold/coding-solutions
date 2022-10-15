class Solution:
    def mergeTrees(self, root1, root2):
        """
        DFS
        RUNTIME: 214 ms
        MEMORY: 15.5 MB
        """
        if not root1: return root2
        elif not root2:return root1
        else:
            # DFS
            merged_root =  TreeNode(root1.val + root2.val)
            merged_root.left = self.mergeTrees(root1.left, root2.left)
            merged_root.right = self.mergeTrees(root1.right, root2.right)
            return merged_root
