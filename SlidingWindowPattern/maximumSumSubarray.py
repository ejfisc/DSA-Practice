#! python3
# maximumSumSubarray.py - find the maximum sum of any contiguous subarray of size K

def findMaximumSumSubarray(k, arr):
    maxSum, windowSum = 0, 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # slide the window, no need if less than K elements in window
        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum) # set new max sum
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # slide the window forward

    return maxSum

def main():
    result = findMaximumSumSubarray(2, [2, 3, 4, 1, 5])
    print(f'Maximum sum of a subarray of size K: {result}')

main()