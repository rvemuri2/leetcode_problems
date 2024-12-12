"""
Given the root of a binary tree, 

return the average value of the nodes on each level in the form of an array. 

Answers within 10^-5 of the actual answer will be accepted. 


                    3
            9               20
                    15              7

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]



initialize queue

while queue:
    level = []
    for i in range(len(queue)):



"""
from collections import deque
def average(root):

    queue = deque([root])
    res = []

    while queue:
        level = []
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr:
                level.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            
        if(level):
            res.append(sum(level) / len(level))
    
    return res

"""
Level Order Traversal but Bottom ot Top

root = [3,9,20,null,null,15,7]
outut -> [[15,7],[9,20],[3]]

"""

from collections import deque
def average(root):

    queue = deque([root])
    res = []

    while(len(queue) > 0):
        level = []
        for i in range(len(queue)):
            curr = queue.popleft()
            if(curr):
                level.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            
        if level:
            res.append(level)
    
    res.reverse()
    return res


"""
Populate right-neighbor pointer

                    3 -->(X)
            9  ->               20 ->(X)
                    15 ->             10 -> (X)

node.val
node.left
node.right
node.next (THIS IS NEW AND WE WANT TO POPULATE IT)
"""

from collections import deque
def average(root):

    queue = deque([root])
    res = []

    while(len(queue) > 0):
        for i in range(len(queue)):
            curr = queue.popleft()
            if(curr):
                queue.append(curr.left)
                queue.append(curr.right)
        
        for index, curr in enumerate(queue):
            if index + 1 >= len(queue):
                curr.next = None
            curr.next = queue[index + 1]
        # level ends
        
    
    return root



"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

https://leetcode.com/problems/average-of-levels-in-binary-tree/

"""