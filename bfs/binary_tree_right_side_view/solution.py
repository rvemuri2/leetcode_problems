# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        
        q = deque()

        q.append(root)
        stack = []

        while(len(q) > 0):
            right = None
            for i in range(len(q)):
                curr = q.popleft()
                if(curr):
                    right = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if(right):
                stack.append(right.val)
        
        return stack