'''
Problem: Given an unsorted array with repetitions, the task is to group multiple
         occurrence of individual elements. The grouping should happen in a way
         that the order of first occurrences of all elements is maintained.

Technique: Create an Ordered dictionary with keys as elements as they appear and
           value as the number of times they appear in the input

Runtime: O(n)

URL: http://www.geeksforgeeks.org/group-multiple-occurrence-of-array-elements-ordered-by-first-occurrence/

Other resources:
===============

- Why Python does not include a ordered dict by default? (http://stackoverflow.com/a/13355382)

'''

from collections import OrderedDict

input_array = map(int, raw_input().strip().split(" "))
numbersCount = OrderedDict()
output = ""

for i in input_array:
    numbersCount[i] = numbersCount.setdefault(i, 0) + 1

for (num, count) in numbersCount.iteritems():
    output += (str(num)+" ")*count

print output.strip()
