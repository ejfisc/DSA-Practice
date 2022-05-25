#! python3
# Given an array, find the average of all subarrays of 'K' contiguous elements in it

def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # slide the window forward, no need to slide if we've not hit the required window size of 'K'
        if windowEnd >= K - 1:
            result.append(windowSum / K) # calculate the average
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # slide the window ahead

    return result

def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print(f'Averages of subarrays of size K: {result}')

main()