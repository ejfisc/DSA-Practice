#! python3
# tripletSumToZero.py - given an unsorted integer array, find all unique triplets in it that add up to 0

def findZeroTriplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]: # skip same element to avoid duplicate triplets
            continue
        findZeroPair(arr, -arr[i], i+1, triplets)

    return triplets

def findZeroPair(arr, targetSum, left, triplets):
    right = len(arr) - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            triplets.append([-targetSum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1 # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1 # skip same element to avoid duplicate triplets
        elif targetSum > currentSum:
            left += 1 # need a pair with a bigger sum
        else:
            right -= 1 # need a pair with a smaller sum

def main():
    print(findZeroTriplets([-3, 0, 1, 2, -1, 1, -2]))
    print(findZeroTriplets([-5, 2, -1, -2, 3]))

main()