#! python3
# Given a string and a pattern, find out if the string contains any permutation of the pattern.

def find_permutation(string, pattern):
    patternDict = {}
    windowStart, matched = 0, 0

    for character in pattern:
        patternDict.setdefault(character, 0)
        patternDict[character] += 1

    for windowEnd in range(len(string)):
        rightChar = string[windowEnd]
        if rightChar in patternDict:
            patternDict[rightChar] -= 1
            if patternDict[rightChar] == 0:
                matched += 1

        if matched == len(patternDict):
            return True

        if windowEnd >= len(pattern) - 1:
            leftChar = string[windowStart]
            windowStart += 1
            if leftChar in patternDict:
                if patternDict[leftChar] == 0:
                    matched -= 1
                patternDict[leftChar] += 1

    return False

    

def main():
    result = find_permutation("oidbcaf", "abc")
    print(result)
    result = find_permutation('odicf', 'dc')
    print(result)

main()