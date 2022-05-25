# Sliding Window Pattern

Used for problems when we are asked to find or calculate something among all the subarrays or sublists of a given size.

For example, consider the problem "given an array, find the average of all subarrays of 'K' contiguous elements in it."

A brute-force algorithm will calculate the sum of each and every 5-element subarray of the given array and divide by K to calculate the average individually. 

Since for every element in the input array, we are calculating the sum of its next 'K' elements, the time complexity of the brute force algorithm will be O(N*K). This algorithm is inefficient because for any two consecutive subarrays of size 'K', the overlapping part will be evaluated twice. 

The efficient way to solve this problem is to visualize each subarray as a sliding window of 'K' elements. To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the sliding window. This saves us from going through the whole subarray to find the sum and as a result the complexity is reduced to O(N).