"""
Quick sort implementation
Best case - O(nlogn)
Worst case - O(n^2)
"""

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot_element = arr[right]

    while i < j:
        # move i pointer until you found a value > pivot value
        while i < right and arr[i] < pivot_element:
            i += 1

        # move the j pointer until you found a value < pivot value
        while j > left and arr[j] >= pivot_element:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot_element:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def quick_sort(arr, left, right):
    # sort if the list >= 2
    if left < right:
        # get the position of the pivot element
        pivot = partition(arr, left, right)
        # quick sort elements to the left of the pivot element
        quick_sort(arr, left, pivot-1)
        # quick sort elements to the right of the pivot element
        quick_sort(arr, pivot+1, right)


li = [1, 8, 3, 7, 2, 4, 12, 11, 15, 14, 5, 6, 0]
quick_sort(li, 0, len(li)-1)
print(li)
