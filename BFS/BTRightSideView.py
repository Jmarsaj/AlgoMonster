from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_right_side_view(root: Node) -> List[int]:
	res = []
	queue = deque([root])
	while len(queue) > 0:
		n = len(queue)
		res.append(queue[0].val)
		for _ in range(n):
			node = queue.popleft()
			for child in [node.right, node.left]:
				if child is not None:
					queue.append(child)
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
    res = binary_tree_right_side_view(root)
    print(' '.join(map(str, res)))

