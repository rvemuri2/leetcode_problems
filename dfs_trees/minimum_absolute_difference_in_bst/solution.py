class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int: # type: ignore

        prev = None
        res = float('inf')

        def dfs(root):

            if not root:
                return
            
            dfs(root.left)
            nonlocal prev, res
            if prev:
                res = min(res, root.val - prev.val)
            
            prev = root

            dfs(root.right)
            

        
        dfs(root)

        return res