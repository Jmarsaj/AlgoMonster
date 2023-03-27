# https://algo.monster/problems/valid_bst
from math import inf

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
	def dfs(root, min_val, max_val):
	# empty nodes are always valid
		if not root:
			return True
		if not (min_val < root.val < max_val):
			return False
		# Note on the logic in the last line of the DFS: when we recursively call DFS on the left node, since the left child's value should be less than or equal to current node's value we should pass current node's value as max value. Vice versa for right recursive call.
		return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
	return dfs(root, -inf, inf)

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
    res = valid_bst(root)
    print('true' if res else 'false')

