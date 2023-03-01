def peakOfMountainArray(list):
	length = len(list) - 1
	left, right = 0, length
	peak = -1
	while (left<=right):
		mid = (left+right) // 2
		if list[mid] > list[mid+1] or mid == length:
			peak = mid
			right = mid - 1
		else:
			left = mid + 1
	return peak

res = peakOfMountainArray([10, 20, 30, 40, 30, 20, 10])
print(res)
