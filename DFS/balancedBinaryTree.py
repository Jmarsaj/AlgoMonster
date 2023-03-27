# https://algo.monster/problems/balanced_binary_tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(tree):
	if tree is None:
		return -1
	
	left_height = tree_height(tree.left)
	right_height = tree_height(tree.right)
	
	if (left_height is -1 or right_height is -1):
		return -1 
	if abs(left_height - right_height) > 1:
		return -1
	return max(left_height, right_height) + 1
	
def is_balanced(tree: Node) -> bool:
    return tree_height(tree) != -1

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')

