#! python3
# longestSubstringKDistinct.py - given a string, find the length of the longest
# substring in it with no more than k distinct characters

def longestSubstringKDistinct(k, str1):
    windowStart, maxLength = 0, 0
    charFrequency = {}

    # in the following loop we'll try to extend the range [windowStart, windowEnd]
    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        charFrequency.setdefault(rightChar, 0)
        charFrequency[rightChar] += 1

        # shrink the sliding window, until we are left with K distinct characters in the charFrequency
        while len(charFrequency) > k:
            leftChar = str1[windowStart]
            charFrequency[leftChar] -= 1
            if charFrequency[leftChar] == 0:
                del charFrequency[leftChar]
            windowStart += 1 # shrink the window
        # remember the max length so far
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength


def main():
    print('Longest substring with no more than K distinct characters: ' + str(longestSubstringKDistinct(2, 'araaci')))
    print('Longest substring with no more than K distinct characters: ' + str(longestSubstringKDistinct(1, 'araaci')))
    print('Longest substring with no more than K distinct characters: ' + str(longestSubstringKDistinct(3, 'cbbebi')))

main()