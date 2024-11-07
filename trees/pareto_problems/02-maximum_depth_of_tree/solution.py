# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # type: ignore

        if not root:
            return 0

        queue = deque([root])
        level = 0
        while(queue):
            for i in range(len(queue)):
                curr = queue.popleft()
                if(curr.left):
                    queue.append(curr.left)
                if(curr.right):
                    queue.append(curr.right)
            
            level += 1
        
        return level