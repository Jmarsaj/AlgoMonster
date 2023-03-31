# Time and Space Complexity = O(n)

from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    res = []
    queue = deque([root])
    while len(queue) > 0:
    	n = len(queue)
    	new_level = []
    	for _ in range(n):
    		node = queue.popleft()
    		new_level.append(node.val)
    		for child in [node.left, node.right]:
    			if child is not None:
    				queue.append(child)
    	res.append(new_level)			
    return res

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))
