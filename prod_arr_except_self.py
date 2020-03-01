print("Enter array: ")
arr = [int(i) for i in input().split(" ")]
prod = 1
for i in arr:
	prod *= i
for i,j in enumerate(arr):
	arr[i] = prod/j
print(arr)
