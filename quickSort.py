#!/usr/bin/bash


def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quickSort(left) + [pivot] + quickSort(right)


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Original Array: ", arr)
print("Sorted Array:   ", quickSort(arr))
