# python program to find the maximum sum of a sub array using Kadane's algorithm

arr = [1, 5, -7, 2]
n = 4

max_val = max_current = arr[0]
for i in range(1,n):
        max_current = max(max_current+arr[i], arr[i])
        if max_current > max_val:
            max_val = max_current

print(max_val)
