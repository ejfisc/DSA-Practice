#! python3
# Given a string, find the length of the longest substring which has all distinct characters

def find_longest_distinct_substring(string):
    charSet = set() # use a set because sets don't allow the same item twice
    maxLength, windowStart = 0, 0
    for windowEnd in range(len(string)):
        # while the character is already in the set, shrink the window from the beginning
        # until we are left with a distinct substring
        while string[windowEnd] in charSet:
            charSet.remove(string[windowStart])
            windowStart += 1 # slide the window forward
        charSet.add(string[windowEnd]) # add the character to the set
        maxLength = max(maxLength, windowEnd - windowStart + 1) # remember the max length
    return maxLength

def main():
    result = find_longest_distinct_substring('aabccbb')
    print(f'Length of longest substring: {result}')

main()