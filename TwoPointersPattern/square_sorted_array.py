#! python3
# Given a sorted array, create a new array containing squares of all the numers of the input array in the sorted order

def square_array(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highestSquareIndex = n - 1
    left, right = 0, n - 1
    # Use two pointers at either end of the array, at each step whichever square is bigger is added to the result array
    # and the pointers move to the next/previous number accordingly.
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIndex] = leftSquare
            left += 1
        else:
            squares[highestSquareIndex] = rightSquare
            right -= 1
        highestSquareIndex -= 1

    return squares    

def main():
    print(square_array([-2,-1,0,2,3]))
    print(square_array([-3,-1,0,1,2]))

main()