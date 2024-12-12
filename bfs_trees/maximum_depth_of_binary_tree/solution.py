# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        
        q = deque([root])

        level = 0
        while(q):
            for i in range(len(q)):
                curr = q.popleft()
                if(curr):
                    q.append(curr.left)
                    q.append(curr.right)
            level += 1
        
        return level - 1