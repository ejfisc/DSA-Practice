#! python3
# Given a string with lowercase letters only, if you are allowed to replace no more than 'k' letters
# with any letter, find the length of the longest substring having the same letters after replacement.

def longest_substring_with_same_letters_after_replacement(K, string):
    characterFrequency = {}
    maxLength, windowStart = 0, 0
    maxRepeatLetterCount = 0
    for windowEnd in range(len(string)):
        rightChar = string[windowEnd]
        characterFrequency.setdefault(rightChar, 0) # insert character into frequency map
        characterFrequency[rightChar] += 1 # increment character frequency
        maxRepeatLetterCount = max(maxRepeatLetterCount, characterFrequency[rightChar]) # remember the maximum frequency
        
        # current window size is from windowStart to windowEnd, overall we have a letter which is repeating maxRepeatLetterCount
        # times, this means we can have a window which has one letter repeating maxRepeatLetterCount times and the remaining
        # letters we should replace. If the remaining letters are more than K, it is time to shrink the window as we are not
        # allowed to replace more than K letters
        if (windowEnd - windowStart + 1 - maxRepeatLetterCount) > K:
            leftChar = string[windowStart]
            characterFrequency[leftChar] -= 1 # decrement the character frequency
            windowStart += 1 # slide the window forward

        maxLength = max(maxLength, windowEnd - windowStart + 1) # remember the max length

    return maxLength
        


def main():
    result = longest_substring_with_same_letters_after_replacement(2, 'aabccbb')
    print(f'Length of substring: {result}')

main()