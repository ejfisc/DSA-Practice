#! python3
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

def find_pair(nums, target):
    # At every iteration we check to see if the sum is greater or less than the target,
    # if the sum is greater than, decrement the end pointer, if the sum is less than
    # increment the start pointer. If the sum is equal to the target, we have our pair.
    start, end = 0, len(nums) - 1
    while start != end:
        pairSum = nums[start] + nums[end]
        if pairSum > target:
            end -= 1
        elif pairSum < target:
            start += 1
        else:
            return [start, end]
    
    return [-1,-1]

def find_pair_alternate(nums, target):
    # Iterate through the array one number at a time, for each number 'x', we need to find 'y' such that 'x + y = target'
    # At each iteration we will search for 'y' (which is equivalent to 'target - x') in the hashtable, if it is there, we 
    # have found the required pair. Otherwise, insert 'x' into the hashtable so that we can search for it later.
    table = {}
    for num in range(len(nums)):
        x = nums[num]
        y = target - x
        if y not in table:
            table.update({x: num})
        else:
            return [table[y], num]

    return [-1,-1]


def main():
    print(find_pair([1,2,3,4,6], 6))
    print(find_pair([2,5,9,11], 11))
    print(find_pair_alternate([2,5,9,11], 11))
    print(find_pair_alternate([1,2,3,4,6], 6))
    

main()