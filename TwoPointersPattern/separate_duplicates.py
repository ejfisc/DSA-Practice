#! python3
# Given an array of sorted numbers, separate all duplicates from it in-place. You should not use any extra space; move all duplicates
# at the end of the array and after moving return the length of the subarray that has no duplicate in it.

def separate_duplicates(arr):
    # we will keep one pointer for iterating the array and one pointer for placing the next non duplicate number. Our algorithm will
    # be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we've seen.
    nextNonDuplicate = 1
    i = 0

    # this will result in an array where the first section is distinct numbers and after that are all of the duplicates that have been
    # "removed"
    while i < len(arr):
        # if there is no duplicate, move the nextNonDuplicate pointer forward
        if arr[nextNonDuplicate - 1] != arr[i]:
            arr[nextNonDuplicate] = arr[i]
            nextNonDuplicate += 1
        i += 1 # move the next pointer forward

    # nextNonDuplicate signifies the end of the distinct numbers, so this is the length of the subarray with no duplicates
    return nextNonDuplicate 


def main():
    print(separate_duplicates([2,3,3,3,6,9,9]))
    print(separate_duplicates([2,2,2,11]))

main()