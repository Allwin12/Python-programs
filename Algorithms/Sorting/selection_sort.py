"""
Selection sort python implementation
O(n^2)
"""

def selection_sort(li):
    for i in range(0, len(li)):
        curr_min = li[i]
        min_index = i
        for j in range(i + 1, len(li)):
            if li[j] < curr_min:
                curr_min = li[j]
                min_index = j
        if curr_min < li[i]:
            li[i], li[min_index] = li[min_index], li[i]


arr = [3, -6, 0, 1, 5, -2]
selection_sort(arr)
print(arr)

# [-6, -2, 0, 1, 3, 5]
