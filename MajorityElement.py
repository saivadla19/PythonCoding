nums = [3,2,3]
nums_length = len(nums)/2
print (list(set(filter(lambda x: nums.count(x) > nums_length , nums))))
