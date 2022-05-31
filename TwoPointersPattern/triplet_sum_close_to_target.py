#! python3
# Given an array of unsorted numbers, find a triplet in the array whose sum is as close to the target as possible, 
# return the sum of the triplet. If there are more than one such triplet, return the triplet with the smallest sum

from math import inf

def find_triplet(arr, target):
    smallestDifference = inf
    # sort the array
    arr.sort()

    # iterate through the array one by one like in triplet sum to zero, but instead of looking for a pair, we will remember the
    # the sum for each triplet
    for i in range(len(arr)):
        start, end = i + 1, len(arr) - 1
        while start < end:
            tripletSum = arr[i] + arr[start] + arr[end]
            # found triplet with sum equal to target
            if tripletSum == target:
                return tripletSum
            diff = target - tripletSum
            # if this was the smallest difference, remember this as the closest sum
            if abs(diff) < abs(smallestDifference) or (abs(diff) == abs(smallestDifference) and diff > smallestDifference):
                smallestDifference = diff
            if tripletSum < target:
                start += 1
            else:
                end -= 1

    return target - smallestDifference

    

def main():
    print(find_triplet([-2, 0, 1, 2], 2))
    print(find_triplet([-3, -1, 1, 4], 1))
    print(find_triplet([1, 0, 1, 1], 100))

main()    