#! python3
# longestSubstringDistinct.py - given a string, find the length of the longest substring
# which has all distinct characters

from turtle import right


def longestSubstringDistinct(str1):
    windowStart, maxLength = 0, 0
    charFrequency = {}

    # try to extend the range [windowStart, windowEnd]
    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        # if the map already contains the 'rightChar', shrink the window from the beginning
        # so that we have only one occurence of 'rightChar'
        if rightChar in charFrequency:
            # we will not have any 'rightChar' after its previous index and if windowStart is already ahead
            # of the last index of rightChar, we'll keep windowStart
            windowStart = max(windowStart, charFrequency[rightChar] + 1)
        # insert rightChar into the map
        charFrequency[rightChar] = windowEnd
        # remember the max length so far
        maxLength = max(maxLength, windowEnd - windowStart + 1)

    return maxLength

def main():
    print('Length of the longest distinct substring: ' + str(longestSubstringDistinct('aabccbb')))
    print('Length of the longest distinct substring: ' + str(longestSubstringDistinct('abbbb')))
    print('Length of the longest distinct substring: ' + str(longestSubstringDistinct('abccde')))

main()