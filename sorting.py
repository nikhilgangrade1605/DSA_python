#bubble sort:

# n = int(input())

# arr = list(map(int, input().split()))

# swaps = 0

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             swaps += 1

# print("Sorted:", *arr)
# print("Swaps:", swaps)


#selection sort:

n = int(input())

arr = list(map(int, input().split()))

swaps = 0

for i in range(n - 1):

    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1

print("Sorted:", *arr)
print("Swaps:", swaps)