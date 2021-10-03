def bubble_sort(arr, reverse=False):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            sort = False
            if reverse and arr[i] < arr[j]:
                sort = True
            elif not reverse and arr[i] > arr[j]:
                sort = True

            if sort:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr


li = [1, 4, 5, 3, 2]
print(bubble_sort(li, reverse=True))
print(bubble_sort(li))
