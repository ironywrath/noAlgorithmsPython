from __future__ import print_function

import numpy as np

def quick_sort(_array):

    #做法：

    '''
        1. 先取數組第一個數，保存為 pivot
        2. 從數組裏對比， 大於pivot的保存一個數組，小於pivot的保存一個數組
        3. 再次運行相同操作在大於數組和小於數組，直到數組的元素數目小於或等於1
        4. 最後一次操作一定是三個數，一個小於，一個大於，然後合并
    '''

    _length = len(_array)
    if (_length <= 1):
        return _array
    else:
        print(_array)
        _pivot = _array[0]
        greater = [ element for element in _array[1:] if element > _pivot]
        lesser = [ element for element in _array[1:] if element <= _pivot ]
        return quick_sort(lesser) + [_pivot] + quick_sort(greater)

i_list1 = [2,5,8,1,3,5,2,0]
print("The original: ", i_list1, '\n')
print(quick_sort(i_list1))

print('\n')

i_list2 = np.random.randint(low = 1, high = 1000, size=100)
print(i_list2, '\n')
print(quick_sort(i_list2))