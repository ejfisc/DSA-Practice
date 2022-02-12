#! python3
# squareSortedArray.py - given a sorted array, create a new array containing the squares of all the numbers
# in the input array in the sorted order, return the array

def squareSortedArray(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highestSquareIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1
    
    return squares
        




def main():
    print(squareSortedArray([-2, -1, 0, 2, 3]))
    print(squareSortedArray([-3, -1, 0, 1, 2]))
    

main()