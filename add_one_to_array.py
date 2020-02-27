# [1,3,5] -> [1,3,6]
# [9,9] -> [1,0,0]

def add_one(arr,last_index):
	if arr[last_index] != 9:
		arr[last_index] += 1
		return arr
	arr[last_index] = 0
	if (last_index*-1) == len(arr):
		arr.insert(0,1)
		return arr
	return add_one(arr,last_index-1)
			


arr = [9,9,9]
print(add_one(arr,-1))
