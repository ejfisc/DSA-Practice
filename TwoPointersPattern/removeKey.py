#! python3
# removeKey.py - given an unsorted integer array and a target 'key', remove all instances of 'key' in-place
# return the new length of the array

def removeKey(arr, key):
    nextElement = 0 # index of the next element which is not 'key'
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1

    return nextElement    

def main():
    print(removeKey([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(removeKey([2, 11, 2, 2, 1], 2))

main()