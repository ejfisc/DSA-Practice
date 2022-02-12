#! python3
# removeDuplicates.py - given a sorted integer array, remove all duplicates in place (w/o using extra memory)
# return the length of the subarray that has no duplicates in it

def removeDuplicates(arr):
    # index of the next non duplicate element
    nextNonDuplicate = 1
    i = 1
    while i < len(arr):
        if arr[nextNonDuplicate - 1] != arr[i]:
            arr[nextNonDuplicate] = arr[i]
            nextNonDuplicate += 1
        i += 1

    return nextNonDuplicate


def main():
    print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
    print(removeDuplicates([2, 2, 2, 11]))

main()