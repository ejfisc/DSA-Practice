#! python3
# Given an array containing 0s and 1s, if you are allowed to replace no more than K 0s with 1s,
# find the length of the longest contiguous subarray having all 1s.

# this is very similar to longest substring with replacement but the only numbers in the array are 1 and 0

def longest_subarray_with_ones_after_replacement(k, arr):
    numberFrequency = {}
    maxLength, windowStart, maxOnesCount = 0, 0, 0
    for windowEnd in range(len(arr)):
        rightNum = arr[windowEnd]
        numberFrequency.setdefault(rightNum, 0) # insert number into frequency map
        numberFrequency[rightNum] += 1 # increment number frequency
        # if this is a 1, remember the maximum frequency
        if rightNum == 1:
            maxOnesCount = max(maxOnesCount, numberFrequency[rightNum])

        # if we have more than k remaining 0s, we should shrink the window
        if (windowEnd - windowStart + 1 - maxOnesCount) > k:
            leftNum = arr[windowStart]
            numberFrequency[leftNum] -= 1 # decrement number frequency
            windowStart += 1 # slide the window forward

        maxLength = max(maxLength, windowEnd - windowStart + 1) # remember the maximum window length

    return maxLength
        

def main():
    result = longest_subarray_with_ones_after_replacement(2, [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1])
    print(f'length of longest subarray: {result}')

main()