"""
Insertion sort implementation using python
Compare each element with all its previous elements and insert in its place
O(n^2)
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


li = [5, 3, 1, 2, 0, 4]
insertion_sort(li)
print(li)
