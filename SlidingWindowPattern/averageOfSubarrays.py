#! python3
# averageOfSubarrays.py - given an array, find the average of subarrays of K contiguous elements in the array
# sliding window implementation

def findAveragesOfSubarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # slide the window, no need to slide if we haven't got K elements in the window yet
        if windowEnd >= K - 1:
            result.append(windowSum / K) # calculate the average
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # slide the window forward

    return result

def main():
    result = findAveragesOfSubarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print(f'Averages of subarrays of size K: {result}')

main()