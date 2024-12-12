from collections import deque
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int: # type: ignore

        q = deque([root])

        if not root:
            return 0

        level = 0
        while(q):
            level += 1
            for i in range(len(q)):
                curr = q.popleft()
                if(not curr.right and not curr.left):
                    return level
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
        
        return level