# Question

# Same as DFS: see that

# Answer 

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        q = deque([node])
        cloned = {node : Node(node.val, None)}

        while q:
            clone = q.popleft()
            for nbr in clone.neighbors:

                if nbr not in cloned:
                    cloned[nbr] = Node(nbr.val, None)
                    q.append(nbr)

                cloned[clone].neighbors.append(cloned[nbr])

        return cloned[node]