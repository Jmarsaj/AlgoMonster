from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zig_zag_traversal(root: Node) -> List[List[int]]:
	res = []
	queue = deque([root])
	left_to_right = True
	while len(queue) > 0:
		n = len(queue)
		new_level = deque()
		for _ in range(n):
			node = queue.popleft()
			if left_to_right:
				new_level.append(node.val)
			else:
				new_level.appendleft(node.val)
			for child in [node.left, node.right]:
				if child is not None:
					queue.append(child)
		res.append(new_level)
		left_to_right = not left_to_right
		
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
    res = zig_zag_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))

