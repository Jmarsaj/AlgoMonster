def firstOccurrenceOfTarget(list, target):
	left, right = 0, len(list) - 1
	index = -1
	while left<=right:
		mid = (left+right) // 2
		if list[mid] == target:
			right = mid - 1
			index = mid
		elif list[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return index
	
res = firstOccurrenceOfTarget([1, 2, 4, 4, 4, 5, 6, 8], 4)
print(res)
