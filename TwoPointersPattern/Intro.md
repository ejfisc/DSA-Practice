# Two Pointers Pattern

Used where we deal with sorted arrays/linked lists and need to find a set of elements that fulfill certain constraints.

For example, consider the problem "Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target."

A brute force algorithm to solve this problem is to consider each element one by one and iterate through the remaining elements to find a pair with the given sum. The time complexity of this algorithm is O(N^2).

Given that the array is sorted there is a more efficient method. Start with one pointer in the beginning and another pointer at the end. At every step, we will see if the numbers pointed by the two pointers add up to the target sum. If they do not, we will do one of two things:
    1. If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum, so we decrement the end-pointer.
    2. If the sum of the two numbers pointed by the two pointers is less than the target sum, this means that we need a pair with a larger sum, so we increment the start-pointer.
The time complexity of this algorithm is reduced to O(N).