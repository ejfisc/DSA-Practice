#! python3
# pairWithTargetSum.py - given a sorted integer array and a target sum, find a pair in the array whose
# sum is equal to the given target. Return the indices of the two numbers

def pairWithTargetSum(arr, targetSum):
    left, right = 0, len(arr) - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            return [left, right]
        
        if targetSum > currentSum:
            left += 1
        else:
            right -= 1
    return [-1, -1]


def main():
    print('Index pair in the array that adds up to sum: ' + str(pairWithTargetSum([1, 2, 3, 4, 6], 6)))
    print('Index pair in the array that adds up to sum: ' + str(pairWithTargetSum([2, 5, 9, 11], 11)))

main()