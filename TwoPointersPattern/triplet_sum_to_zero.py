#! python3
# Given an array of unsorted numbers, find all unique triplets in it that add up to 0

def find_triplets(arr):
    triplets = []
    # sort the array
    arr.sort()

    # iterate through the array one by one, at every iteration we have 'x' and are looking for 'y' and 'z' such that
    # 'x + y + z = 0'. We can use a similar method from pair with target sum to find a pair with sum '-x'
    for i in range(len(arr)):
        x = arr[i]
        # skip duplicates
        if i > 0 and x == arr[i-1]:
            continue
        target = -x
        start, end = i + 1, len(arr) - 1
        while start < end:
            y, z = arr[start], arr[end]
            pairSum = y + z
            # found the triplet
            if pairSum == target:
                triplets.extend([[x, y, z]])
                start += 1
                end -= 1
                # skip duplicates
                while start < end and arr[start] == arr[start - 1]:
                    start += 1
                while start < end and arr[end] == arr[end + 1]:
                    end -= 1
            elif pairSum < target:
                start += 1 # need a pair with a bigger sum
            else:
                end -= 1 # need a pair with a smaller sum

    return triplets



def main():
    print(find_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(find_triplets([-5, 2, -1, -2, 3]))

main()
    