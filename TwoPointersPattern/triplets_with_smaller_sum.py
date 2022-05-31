#! python3
# Given an array of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target
# where i, j, and k are 3 different indices. Return the count of such triplets.

def count_smaller_triplets(arr, target):
    triplets = 0
    # sort the array
    arr.sort()

    # iterate through the array one by one. at each iteration we will search for a pair whose sum is less than target - arr[i]
    for i in range(len(arr)-2):
        j, k = i + 1, len(arr) - 1
        while j < k:
            if arr[j] + arr[k] < target - arr[i]: # found the triplet
                # since the array is sorted and arr[k] >= arr[j], we dcan replace arr[k] by any 
                # number between j and k to get a sum less than the target sum
                triplets += k - j
                j += 1
            else:
                k -= 1 # we need a pair with a smaller sum

    return triplets

def main():
    print(count_smaller_triplets([-1,0,2,3], 3))
    print(count_smaller_triplets([-1,4,2,1,3], 5))

main()