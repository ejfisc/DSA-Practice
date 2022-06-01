#! python3
# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose
# product is less than the target number. 

from collections import deque

def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    # this problem uses sliding window and two pointer
    # this main for loop manages the sliding window
    for right in range(len(arr)):
        product *= arr[right]
        # shrink the window
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
        # since the product of all numbers from left to right is less than the target
        # therefore, all subarrays from left to right will have a product less than the
        # target too; to avoid duplicates, we will start with a subarray containing only
        # arr[right] and then extend it
        subarray = deque()
        for i in range(right, left-1, -1):
            subarray.appendleft(arr[i])
            result.append(list(subarray))
    return result

            

def main():
    print(find_subarrays([2,5,3,10], 30))
    print(find_subarrays([8,2,6,5], 50))

main()