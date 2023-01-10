
# Q4. Write a function that takes a list of strings and returns a new list with all strings that are anagrams
# of a palindrome (i.e., a word or phrase that can be rearranged to form a palindrome).
# If you can use list comprehension then it will be better.


# Sample Input output

# Input: ['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']
# Output: ['carcare', 'carecar', 'vicic']

# Explanation - carecar and carecar are anagrams of a palindrome racecar.
# vicic is an anagram of palindrome civic. lehol is anagram of hello, but hello is not a palindrome,
# hence lehol is not in the output.


def is_palindrome(s):
    return s == s[::-1]


def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


input_strings = ['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']
output = list()
for word1 in input_strings:
    if is_palindrome(word1):
        [output.append(word2) for word2 in input_strings if word1 != word2 and check_anagram(word1, word2)]

print(output)
