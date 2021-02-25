import itertools
nums = [-1,0,1,2,-1,-4]
NumsCombinations = list(filter(lambda x: sum(x) == 0, itertools.combinations(nums,3)))
print (NumsCombinations)