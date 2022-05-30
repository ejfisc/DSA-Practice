#! python3
# Given a string and a pattern, find all anagrams of the pattern in the given string

def find_anagrams(str1, pattern):
    charFrequency = {}
    matched, windowStart = 0, 0
    anagrams = []

    for char in pattern:
        charFrequency.setdefault(char, 0)
        charFrequency[char] += 1

    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        if rightChar in charFrequency:
            charFrequency[rightChar] -= 1
            if charFrequency[rightChar] == 0:
                matched += 1

        if matched == len(charFrequency):
            anagrams.append(windowStart)

        if windowEnd >= len(pattern) - 1:
            leftChar = str1[windowStart]
            windowStart += 1
            if leftChar in charFrequency:
                if charFrequency[leftChar] == 0:
                    matched -= 1
                charFrequency[leftChar] += 1

    
    return anagrams

def main():
    result = find_anagrams('ppqp', 'pq')
    print(f'Anagram indeces: {result}')
    result = find_anagrams('abbcabc', 'abc')
    print(f'Anagram indeces: {result}')

main()
