def minimumInSortedRotatedArray(list):
	left, right = 0, len(list)-1
	min_index = -1
	while (left<=right):
		mid = (left+right) // 2
		if (list[mid] <= list[-1]):		#list[-1] is the last element in list
			min_index = mid
			right = mid - 1
		else:
			left = mid + 1
	return min_index
		
res = minimumInSortedRotatedArray([30, 40, 50, 10, 20])
print(res)
			
