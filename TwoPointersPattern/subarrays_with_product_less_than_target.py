#! python3
# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose
# product is less than the target number. 

def find_subarrays(arr, target):
    subarrays = []
    windowStart = 0

    # This problem follows sliding window and two pointers pattern
    # we will use a sliding window to iterate through the array
    # for each window, use two pointer to calculate the product of the subarray
    for windowEnd in range(len(arr)):
        product = 0
        left, right = windowStart, windowEnd
        while left < right:
            product += arr[left] * arr[right]
            left += 1
            right -= 1
        # if the window is 1 element long and that element is less than target, add it to the list
        if windowStart == windowEnd and arr[windowStart] < target:
            subarrays.append([arr[windowStart]])
        # if the product of the window is less than the target, add it to the list
        if product < target:
            subarrays.append([arr[windowStart:windowEnd]])
        elif product > target:
            # move the window forward
            windowStart += 1

    return subarrays
            

            

def main():
    print(find_subarrays([2,5,3,10], 30))
    print(find_subarrays([8,2,6,5], 50))

main()