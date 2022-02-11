#! python3
# smallestSubarrayWithGreaterSum.py - find the smallest contiguous subarray whose sum is greater than or equal to S

def findSmallestSubarrayWithGreaterSum(S, arr):
    windowSum, windowStart = 0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        if windowSum < S:
            continue