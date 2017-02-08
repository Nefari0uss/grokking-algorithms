#!/usr/bin/python3


def merge_sort(arr):
    if len(arr) > 1:

        # sub-divide into partitions
        mid = len(arr) // 2
        left = arr[:mid]  # from 0 to mid
        right = arr[mid:]  # from mid to end

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0  # i is left, j is right, k is the original array

        # keep sorting until only 1 table is left with elements
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # sort the remaining element(s)

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Original array: ", arr)
print("Sorted Array:   ", merge_sort(arr))
