#! python3
# Given an array of positive numbers and a positive number 'K', find the maximum sum of any
# contiguous subarray of size 'K'

def find_maximum_sum_subarray(K, arr):
    result = 0.0
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # slide the window forward, no need to slide if we've not hit 'K' elements
        if windowEnd >= K - 1:
            result = max(result, windowSum) # find the max sum
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # slide the window ahead

    return result


def main():
    result = find_maximum_sum_subarray(3, [-1, -3, -4, -2, 0, -10])
    print(f'Maximum Sum: {result}')

main()