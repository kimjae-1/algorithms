#dfs(깊이우선탐색)
# using recursion
# 전위순회, 중위순회, 후위순회

def dfs(cur_node):
    if cur_node is None:
        return
    dfs(cur_node.left)
    dfs(cur_node.right)
    

# preorder - 자식 노드 방문 전, 부모 노드 먼저 방문 
def preorder(cur_node):
    if cur_node is None:
        return
    
    print(cur_node.vlaue)
    preorder(cur_node.left)
    preorder(cur_node.right)
    
# inorder - 
def inorder(cur_node):
    if cur_node is None:
        return
    
    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)
    
# postorder
def postorder(cur_node):
    if cur_node is None:
        return
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)