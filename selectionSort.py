#!/usr/bin/python3


def getSmallestIndex(arr):
    smallestValue = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallestValue:
            smallestValue = arr[i]
            smallestIndex = i
    return smallestIndex


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        newArr.append(arr.pop(getSmallestIndex(arr)))
    return newArr


array = [5, 3, 6, 2, 10]
print("Original Array: ", array)
print("Sorted Array  : ", selectionSort(array))
