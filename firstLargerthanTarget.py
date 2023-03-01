def firstLargerthanTarget(list, target):
    left, right = 0, len(list) - 1
    boundary = -1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] >= target:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary 

res = firstLargerthanTarget([1, 3, 4, 6, 7, 9, 10], 2)
print(res)