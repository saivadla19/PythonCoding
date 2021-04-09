'''
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.ss

'''


import itertools 
deliciousness = [1,1,1,3,3,3,7]
foodCombinations = list(itertools.combinations(deliciousness,2))
op = []
def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0

for i in foodCombinations:
    if ( is_power_of_two(sum(i)) == True):
        op.append(i)

print (len(op))