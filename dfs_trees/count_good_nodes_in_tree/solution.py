class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.good = 0

        def dfs(root, maxVal):

            if not root:
                return
            
            if(root.val >= maxVal):
                self.good += 1

            maxVal = max(maxVal, root.val)
            
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, root.val)
        return self.good