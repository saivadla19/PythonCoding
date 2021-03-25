'''
problem:

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example: Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

'''

num = "10200"
k = 1
counter = 0
op = []
for i in num:
    op.append(num[:counter] + num[k:])
    counter = counter + 1
    k = k + 1
op = "".join(min(op).lstrip('0'))
print (op)

