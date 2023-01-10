# Q5. Write a function or lambda function (preferably) that takes a list of strings
# and returns a new list with all strings sorted in descending order of length.

# Input: ["dog", "cat", "bird"]
# Output: ['bird', 'cat', 'dog']

# Input: ["python", "java", "c++"]
# Output: ["python", "java", "c++"]

def sorting(lst, order):
    return sorted(lst, key=lambda x: len(x), reverse=order)


inputList = ["dog", "cat", "bird"]
# inputList = ["python", "java", "c++"]
newList = sorting(inputList, True)
print("original list: ", inputList)
print("Descending order sorted list: ", newList)

