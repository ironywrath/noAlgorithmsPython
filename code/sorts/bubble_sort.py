from __future__ import print_function

import numpy as np

def bubble_sort(collection):

    length = len(collection) #先取得數據的長度

    for i in range(length):
        for j in range(length):
            if collection[j] > collection[i]:
                i_temp = collection[i]
                collection[i], collection[j] = collection[j], i_temp

    return collection

i_list1 = [22,55,11,77,22,33,44,88,11]
i_list2 = [22,55,66,77,11,33,44,88,99]
print(bubble_sort(i_list2))
print(bubble_sort(i_list1))

i_list3 = np.random.randint(low = 1, high = 1000, size=100)
print(i_list3)
print(bubble_sort(i_list3))
