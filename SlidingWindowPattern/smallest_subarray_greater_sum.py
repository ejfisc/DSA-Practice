#! python3
# Given an array of positive numbers and a positive number 'S,' find the length of the smallest
# contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no subarray exists.
import math

def find_smallest_subarray_with_greater_sum(S, arr):
    minLength = math.inf
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # add elements to the window until the sum >= S
        # shrink the window from the beginning until sum < S
        while windowSum >= S:
            minLength = min((windowEnd + 1) - windowStart, minLength) # calculate min length
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # move the window forward

    if minLength == math.inf:
        return 0
    return minLength

def main():
    result = find_smallest_subarray_with_greater_sum(7, [2, 1, 5, 2, 3, 2])
    print(f'Length of smallest subarray: {result}')

main()