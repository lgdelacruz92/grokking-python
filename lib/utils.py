from typing import List, Optional
from lib.tree_node import TreeNode
from collections import deque

def print_tree_node(node: Optional[TreeNode]):
    if not node:
        return
    
    q = deque()
    q.append((node, 0))
    while q:
        next_node, level = q.popleft()
        prefix = ''
        for i in range(level):
            prefix += '-'
        print(f'{prefix}{next_node.val}')
        if next_node.left:
            q.append((next_node.left, level+1))
        
        if next_node.right:
            q.append((next_node.right, level+1))


def make_tree_node_from_array(arr: List[Optional[int]]) -> Optional[TreeNode]:
    # [5,4,8,11,null,13,4,7,2,null,null,5,1]
    # left: 2i + 1
    # right: 2i
    n = len(arr)
    if n == 0:
        return None
    arr_nodes = []
    for i in range(n):
        num = arr[i]
        if num != None:
            node = TreeNode(num)
            arr_nodes.append(node)
        else:
            arr_nodes.append(None)
    
    # arr_nodes: same as arr but in node format
    # connect it's children
    for i, node in enumerate(arr_nodes):
        if i == 6:
            print('here')
        left_child = arr_nodes[i * 2 + 1] if i * 2 + 1 < n else None
        right_child = arr_nodes[i * 2 + 2] if i * 2 + 2 < n else None
        if node:
            node.left = left_child
            node.right = right_child

    return arr_nodes[0]