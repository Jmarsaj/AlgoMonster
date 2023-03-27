def feasible(read_times, workers, limit):
	time, num_workers = 0, 0
	for read_time in read_times:
		if time+read_time > limit:
			time = 0
			num_workers += 1
		time += read_time
	if time != 0:
		num_workers += 1
	return num_workers <= workers



def newspapers(read_times, workers):
	low, high = max(read_times), sum(read_times)
	res = -1
	while (low<=high):
		mid = (low+high) // 2
		if feasible(read_times, workers, mid):
			res = mid
			high = mid - 1
		else:
			low = low + 1
	return res
	
read_times = [int(x) for x in input("Enter read times: ").split()]
workers = int(input("Enter number of workers: "))
print(newspapers(read_times, workers))
