"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node': # type: ignore
        if not root: 
            return None
        
        queue = deque([root])  # Initialize a queue with the root node

        while queue:
            prev = None  # Track the previous node in the same level

            for _ in range(len(queue)):  # Process all nodes in the current level
                curr = queue.popleft()
                if prev:
                    prev.next = curr  # Connect the previous node's next pointer to current node
                prev = curr  # Update previous node to current

                # Add child nodes to the queue for the next level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            prev.next = None  # Ensure the last node in the level points to None

        return root