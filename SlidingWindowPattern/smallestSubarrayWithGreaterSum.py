#! python3
# smallestSubarrayWithGreaterSum.py - find the length of the smallest contiguous subarray whose 
# sum is greater than or equal to S
import math

def findSmallestSubarrayWithGreaterSum(s, arr):
    windowSum, windowStart = 0, 0
    minLength = math.inf
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # shrink the window as small as possible until windowSum < S
        while windowSum >= s:
            minLength = min(minLength, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # slide the window forward
    if minLength == math.inf:
        return 0
    return minLength

def main():
    result = findSmallestSubarrayWithGreaterSum(8, [3, 4, 1, 1, 6])
    print(f'The smallest subarray with a sum greater than or equal to S: {result}')

main()