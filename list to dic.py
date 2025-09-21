
arr = [1, 0, 0, 1, 1, 0, 1, 0]

# Pointer to place next 0
index = 0

# Move all 0s to the front by swapping
for i in range(len(arr)):
    if arr[i] == 0:
        arr[i], arr[index] = arr[index], arr[i]
        index += 1

print(arr)
