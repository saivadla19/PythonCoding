'''
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.
'''

import itertools
arr = [1,-2,1]
k = 5
output = list(itertools.chain(*(itertools.repeat(arr,k))))
print (output)