from __future__ import print_function

import random
import numpy as np

def bogosort(collection):

    count = 0

    def isSorted(collection):
        print("Count: ", count, "Result: " , collection)
        if len(collection) < 2:
            return True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while not isSorted(collection):
        count = count + 1
        random.shuffle(collection)

    return collection

i_list1 = [2,5,8,1,3,5,2,0]
print("The original: ", i_list1, '\n')
print(bogosort(i_list1))

print('\n')

i_list2 = np.random.randint(low = 1, high = 1000, size=10)
print(i_list2, '\n')
print(bogosort(i_list2))

