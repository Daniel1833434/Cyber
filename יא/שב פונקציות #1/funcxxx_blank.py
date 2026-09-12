"""
finds the longest sub string with different characters
"""
def longest_unique_substring(s):
    currentString = ''
    finalReturn= ''
    currentCount=0
    longestCount=0
    for i in range(len(s)):
        currentString =''
        currentCount = 0
        for j in range(i,len(s)):
            if s[j] not in currentString:
                currentString+=s[j]
                currentCount+=1
            else:
                break

        if currentCount > longestCount:
            longestCount = currentCount
            finalReturn = currentString

    return finalReturn

"""
    Determine if x is the majority element in the sorted array arr.

    Args:
        arr (list[int]): The sorted array of integers.
        x (int): The element to check for majority.

    Returns:
        bool: True if x is the majority element, False otherwise.
"""
def is_majority(lst, k):
    dict = {}
    for x in lst:
        if x not in dict:
            dict[x] =1
        else:
            dict[x] += 1
    for key in dict.keys():
        if dict[key] >= dict[k] and key != k:
            return False
    return True


if __name__ == "__main__":

    assert longest_unique_substring("aaxyyzwc") == "yzwc"
    assert longest_unique_substring("bbbb") == "b"
    assert longest_unique_substring("abcde") == "abcde"

    assert is_majority([1, 2, 3, 3, 3, 3, 10], 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 4) == True
    assert is_majority([1, 1, 1, 2, 2], 1) == True
    assert is_majority([1, 1, 2, 2], 1) == False
    assert is_majority([1, 1, 1, 1, 2, 2, 2], 1) == True
    assert is_majority([1, 1, 1, 1, 2, 2, 2], 2) == False