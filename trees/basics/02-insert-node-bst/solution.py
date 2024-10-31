from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # type: ignore

        if not root:
            return TreeNode(val) # type: ignore
        
        if(root.val < val):
            root.right = self.insertIntoBST(root.right, val)
        
        elif(root.val > val):
            root.left = self.insertIntoBST(root.left, val)

        return root 