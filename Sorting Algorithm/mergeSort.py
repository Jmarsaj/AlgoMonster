#Stable sorting (still in relative order)
#Not in-place (using another data structure)
#Time Complexity = 
from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
	n = len(unsorted_list)
	if n <= 1:
		return unsorted_list
	midpoint = n // 2
	left_list, right_list = sort_list(unsorted_list[:midpoint]), sort_list(unsorted_list[midpoint:])
	l_pointer, r_pointer = 0, 0
	result = []
	
	while l_pointer < midpoint or r_pointer < n - midpoint:
		if l_pointer == midpoint:
			result.append(right_list[r_pointer])
			r_pointer += 1
		elif r_pointer == n - midpoint:
			result.append(left_list[l_pointer])
			l_pointer += 1
		elif left_list[l_pointer] <= right_list[r_pointer]:
			result.append(left_list[l_pointer])
			l_pointer += 1
		else:
			result.append(right_list[r_pointer])
			r_pointer += 1
		
	return result 
	
	

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
