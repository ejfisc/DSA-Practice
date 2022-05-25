#! python3
# You're visiting a farm to collect fruits. The farm has a single row of fruit trees. You will
# be given two baskets, and your goal is to pick as many fruits as possible to be
# placed in the given baskets.
# You're given an array of characters where each character represents a fruit tree
# The farm has the following restrictions:
# 1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# 2. You can start with any tree, but you can't skip a tree once you have started.
# 3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have
# to pick from a third fruit type. 
# Write a function to return the maximum number of fruits in both baskets.

# notice that this is very similar to the longest_k_distinct_substring problem. You are essentially looking
# for the longest contiguous substring with K distinct characters where K = 2

def maximum_number_of_fruit(fruit):
    fruitFrequency = {}
    maxLength, windowStart = 0, 0
    for windowEnd in range(len(fruit)):
        rightFruit = fruit[windowEnd]
        fruitFrequency.setdefault(rightFruit, 0) # insert fruit into map
        fruitFrequency[rightFruit] += 1 # increment fruit frequency
        # shrink the window from the beginning until we are left with 2 fruit
        while len(fruitFrequency) > 2:
            leftFruit = fruit[windowStart]
            fruitFrequency[leftFruit] -= 1 # decrement fruit frequency
            # if the fruit's frequency is 0 remove it from the map
            if fruitFrequency[leftFruit] == 0:
                del fruitFrequency[leftFruit]
            windowStart += 1 # move the window ahead
        maxLength = max((windowEnd + 1) - windowStart, maxLength) # calculate the max length

    return maxLength



def main():
    result = maximum_number_of_fruit(['A', 'B', 'C', 'A', 'C'])
    print(f'Max number of fruit in both baskets: {result}')

main()