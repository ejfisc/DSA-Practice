#! python3
# Given a string, find the length of the longest substring in it with no ore than K distinct characters
# you can assume K is less than or equal to the length of the given string

from numpy import char


def find_longest_substring_with_k_distinct_characters(K, string):
    characterFrequency = {}
    maxLength, windowStart = 0, 0
    for windowEnd in range(len(string)):
        rightChar = string[windowEnd]
        characterFrequency.setdefault(rightChar, 0) # insert character into hash map
        characterFrequency[rightChar] += 1 # increment character frequency
        # shrink the window from the beginning until we are left with K characters in the map
        while len(characterFrequency) > K:
            leftChar = string[windowStart]
            characterFrequency[leftChar] -= 1 # decrement character frequency
            # if the character's frequency is 0 remove it from the hash map
            if characterFrequency[leftChar] == 0:
                del characterFrequency[leftChar]
            windowStart += 1 # slide the window forward
        maxLength = max((windowEnd + 1) - windowStart, maxLength) # calculate the max length

    return maxLength
            


def main():
    result = find_longest_substring_with_k_distinct_characters(2, 'araaci')
    print(f'length of longest substring with k characters: {result}')

main()