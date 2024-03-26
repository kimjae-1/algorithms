# BFS 
# que 사용
from collections import deque
    
def bfs(root):
    visited = []
    if root is None:
        return []
    dq = deque()
    dq.append(root)
    
    while dq:
        cur_node = q.popleft()
        visited.append(cur_node.value)
        
        if cur_node.left:
            dq.append(cur_node.left)
        if cur_node.right:
            dq.append(cur_node.right)
        
        return visited