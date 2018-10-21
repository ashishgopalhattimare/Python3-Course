from collections import deque

def tree_by_levels(node):

    result = []     # result array
    dq = deque()    # deque works as both stack and queue
    
    if node == None:
        return result
        
    dq.append(node)
    while len(dq) != 0:
        
        node = dq.popleft()
        result.append(node.value)
        if node.left != None:
            dq.append(node.left)
        if node.right != None:
            dq.append(node.right)
    
    return result