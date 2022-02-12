#! python3
# fruitsIntoBaskets.py - Given an array of characters where each char represents a fruit tree, you're given 2 
# baskets and your goal is to put the max number of fruits in each basket. Each basket can only have 1 fruit type
# return the max number of fruits in both baskets
# (this one is essentially longestSubstringKDistinct, where K = 2)

def fruitsIntoBaskets(trees):
    windowStart, maxFruit = 0, 0
    fruitFrequency = {}

    # in the following loop, we'll try to extend the range [windowStart, windowEnd]
    for windowEnd in range(len(trees)):
        rightFruit = trees[windowEnd]
        fruitFrequency.setdefault(rightFruit, 0)
        fruitFrequency[rightFruit] += 1
        # shrink the sliding window until we are left with 2 distinct types of fruit
        while len(fruitFrequency) > 2:
            leftFruit = trees[windowStart]
            fruitFrequency[leftFruit] -= 1
            if fruitFrequency[leftFruit] == 0:
                del fruitFrequency[leftFruit]
            windowStart += 1 # shrink the window
        # remember the max length so far
        maxFruit = max(maxFruit, windowEnd - windowStart + 1)

    return maxFruit

def main():
    print('Maximum number of fruits in both baskets: ' + str(fruitsIntoBaskets(['A', 'B', 'C', 'A', 'C'])))
    print('Maximum number of fruits in both baskets: ' + str(fruitsIntoBaskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()