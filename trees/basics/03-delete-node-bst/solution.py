# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def findMin(self, root):
        curr = root
        while(curr and curr.left):
            curr = curr.left
            
        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]: # type: ignore
        
        
        if not root:
            return None
        
        if(key > root.val):
            root.right = self.deleteNode(root.right, key)
        elif(key < root.val):
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = self.findMin(root.right)
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)

        return root