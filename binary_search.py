#!/usr/bin/python3

def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while  low <= high:
    index = (low + high) // 2
    num = list[index]
    if num < item:
      low = index + 1
    elif num > item: 
      high = index - 1
    elif num == item:
        return index

  return None


test_list = [1,3,5,7,9]
print(binary_search(test_list, 3))
print(binary_search(test_list, -1))

