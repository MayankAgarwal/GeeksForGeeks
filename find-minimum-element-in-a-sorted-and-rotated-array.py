'''
Problem : Find the minimum element in a rotated sorted array
Technique: Binary search
Runtime: O(logn)

URL: http://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
'''


def find_min (arr, first, mid, last, length):
    
    if arr[mid-1] > arr[mid] < arr[ (mid+1)%length ]:
        return arr[mid]

    # Array not rotated
    if first > last:
        return arr[0]
    
    if arr[first] < arr[mid] or first == mid:
        first = mid + 1

    elif arr[mid] < arr[last] or mid == last:
        last = mid - 1

    mid = int( (first + last)/2 )

    return find_min(arr, first, mid, last, length)


numbers = map(int, raw_input().strip().split(" "))
length = len(numbers)

first = 0
last = length - 1
mid = int( (first+last)/2 )

result = find_min(numbers, first, mid, last, length)

print "Minimum element of rotated sorted list: ", result
