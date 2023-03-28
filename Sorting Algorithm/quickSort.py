# Sorts array in-place (does not require additional data structures)
# Algorithm is not stable as each swap skips many values
# Average time-complexity = O(nlog(n)), Worse time-complexity = O(n^2)
from typing import List

def sort_list_interval(unsorted_list: List[int], start: int, end: int) -> None:
	if end - start <= 1:
		return
	pivot = unsorted_list[end -1]
	start_ptr = start
	end_ptr = end-1
	while start_ptr < end_ptr:
		while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
			start_ptr += 1
		while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
			end_ptr -= 1
		if start_ptr == end_ptr:
			break
		unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]
	unsorted_list[start_ptr], unsorted_list[end-1] = unsorted_list[end-1], unsorted_list[start_ptr]
	sort_list_interval(unsorted_list, start, start_ptr)
	sort_list_interval(unsorted_list, start_ptr + 1, end)
	
	
def sort_list(unsorted_list: List[int]) -> List[int]:
	sort_list_interval(unsorted_list, 0, len(unsorted_list))
	return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
