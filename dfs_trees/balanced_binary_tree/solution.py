from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: # type: ignore

        
        def dfs(root, left, right):

            if not root:
                return True
            
            if not(root.val < right and root.val > left):
                return False
            
            return (dfs(root.left, left, root.val) and dfs(root.right, root.val, right))
            

        return dfs(root, float('-inf'), float('inf'))