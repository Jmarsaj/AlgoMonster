from typing import List
from collections import deque

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
	num_rows, num_cols = len(image), len(image[0])
	def get_neighbors(coord, color):
		r, c = coord
		delta_row = [-1, 0, 1, 0]
		delta_col = [0, 1, 0, -1]
		for i in range(len(delta_row)):
			neighbor_row = r + delta_row[i]
			neighbor_col = c + delta_col[i]
			if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
				if image[neighbor_row][neighbor_col] == color:
					yield neighbor_row, neighbor_col
    
	def bfs(root):
		queue = deque([root])
		visited = [[False for c in range(num_cols)] for r in range(num_rows)]
		r, c = root
		color = image[r][c]
		image[r][c] = replacement
		visited[r][c] = True
		while len(queue) > 0:
			node = queue.popleft()
			for neighbor in get_neighbors(node, color):
				r, c = neighbor
				if visited[r][c]:
					continue
				image[r][c] = replacement
				visited[r][c] = True
				queue.append(neighbor)
	bfs((r, c))
	return image

if __name__ == '__main__':
    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(' '.join(map(str, row)))

