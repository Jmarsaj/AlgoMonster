def squareRootEstimation(n):
	left, right = 1, n-1
	res = -1
	while (left<=right):
		mid = (left+right) // 2
		if mid*mid == n:
			return mid
		elif mid*mid > n:
			res = mid
			right = mid - 1
		else:
			left = mid + 1
	return res - 1
	
n = int(input("Enter a number: "))
res = squareRootEstimation(n)
print(res)
