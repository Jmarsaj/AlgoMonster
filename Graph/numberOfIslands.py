from typing import List
from collections import deque

def count_number_of_islands(grid:List[List[int]]) -> int:
	num_rows, num_cols = len(grid), len(grid[0])
	
	def get_neighbors(coord):
		r, c = coord
		delta_row = [-1, 0, 1, 0]
		delta_col = [0, 1, 0, -1]
		res = []
		for i in range(len(delta_row)):
			neighbor_row = r + delta_row[i]
			neighbor_col = c + delta_col[i]
			if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
				res.append((neighbor_row, neighbor_col))
		return res
		
	def bfs(root):
		queue = deque([root])
		r, c = root
		grid[r][c] = 0
		while len(queue) > 0:
			node = queue.popleft()
			for neighbor in get_neighbors(node):
				r, c = neighbor
				if grid[r][c] == 0:
					continue
				grid[r][c] = 0
				queue.append(neighbor)
	
	count = 0
	for r in range(num_rows):
		for c in range(num_cols):
			if grid[r][c] == 0:
				continue
			bfs((r, c))
			count += 1
			
	return count
	
if __name__ == '__main__':
	grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
	res = count_number_of_islands(grid)
	print(res)
